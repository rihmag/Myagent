from langchain_core.messages import ToolMessage,AIMessage
from states.state import State

class Combine:
    def __init__(self,llm,tools):
        self.llm=llm
        self.tools=tools
    def call_tool(self,state: State) -> dict:
        """
        Node to execute a tool if the LLM has decided to call one.
        It takes the last AI message (which should contain tool calls) and executes them.
        """
        import json
        print("--- Node: call_tool ---")
        last_message = state["messages"][-1]
        print("this tool call in tools combine",last_message.additional_kwargs.get("tool_calls")[0].get("function").get("name"))
        tool_outputs = []
        # OpenAI model with tool_calls
        if last_message.additional_kwargs.get("tool_calls"):
            tool_call = last_message.additional_kwargs["tool_calls"][0]
            tool_name = tool_call["function"]["name"]
            raw_arguments = tool_call["function"]["arguments"]
            
            print(f"Executing tool: {tool_name} with raw input: {raw_arguments}")
            
            # Parse JSON arguments
            try:
                tool_input = json.loads(raw_arguments)

            except json.JSONDecodeError:
                print("Error: Tool arguments are not valid JSON.")
                tool_input = {}

            # Find the tool by name
            selected_tool = next((t for t in self.tools if t.name == tool_name), None)

            if not selected_tool:
                print(f"Tool {tool_name} not found.")
            else:
                # Call the tool with unpacked arguments
                output = selected_tool.invoke(input={**tool_input})

                print(f"Final tool output: {output}")

                # Represent output as AI message
                tool_outputs.append(AIMessage(content=f"Tool output: {output}"))
 # Represent as AI message for simplicity
    
        # Basic parsing for Ollama if it tried to output JSON tool call
        elif isinstance(last_message.content, str) and "tool_name" in last_message.content:
            import json
            try:
                tool_call_data = json.loads(last_message.content.strip("`").strip("json").strip()) # Attempt to parse JSON
                tool_name = tool_call_data.get("tool_name")
                tool_input = tool_call_data.get("tool_input", {})
                print(f"Executing Ollama-parsed tool: {tool_name} with input: {tool_input}")
                selected_tool = next(t for t in self.tools if t.name == tool_name)
                output = selected_tool.invoke(tool_input)
                tool_outputs.append(AIMessage(content=f"Tool output: {output}")) # Represent as AI message for simplicity
    
            except (json.JSONDecodeError, StopIteration) as e:
                print(f"Ollama tool parsing failed or tool not found: {e}")
                tool_outputs.append(AIMessage(content=f"Error parsing tool call: {last_message.content}"))
        else:
            print("No tool calls detected or parsed for execution.")
            # If no tool calls, just return the state as is, or an error message
            # For simplicity, we assume an error or a direct answer was intended by LLM
            pass
            
        return {"messages": tool_outputs}
    