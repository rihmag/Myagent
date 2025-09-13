from states.state import State
class Condition():
    def __init__(self,llm):
        self.keywords=  ["support", "customer care", "help", "talk to agent", "contact support"]
        self.keywords_for_course=["course","courses"]
        self.llm=llm
    def apply_condition(self, state:State):
        last_message = self.llm.invoke(state["messages"])
        print(last_message)
        for step in last_message:
            if hasattr(step, "tool_calls"):
                for tool_call in step.tool_calls:
                    tool_name = tool_call.get("name")
                    tool_args = tool_call.get("args")
                    print(f"Tool called: {tool_name} with args: {tool_args}")
                return "tool_call"

        
        
        # Check if tool_calls exist in the response
        
            
        
    
        
        return "end" # default if no condition matches

                
