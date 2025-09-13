from states.state import State
from langgraph.graph import StateGraph,START,END
from llm.firstllm import Return_llm
from langchain_core.messages import HumanMessage
from nodes.chatbotnode import node
from nodes.sendmail import SendMail
from nodes.condition import Condition
from nodes.course import Course
from tool_invoke.tools_combine import Combine
from langgraph.prebuilt import ToolNode
from langgraph.checkpoint.memory import MemorySaver
memory=MemorySaver()
class FirstGraph:
    def __init__(self,llm):
        sendmail=SendMail().sendmail
        get_courses=Course().get_courses
        self.tools=[sendmail,get_courses]
        self.graph_builder=StateGraph(State)
        self.llm=llm.bind_tools(self.tools)
        
    def graph(self,input):
        condition=Condition(self.llm).apply_condition
        self.graph_builder.add_node("chatbot", node(self.llm).call)
        self.graph_builder.add_node("call_tool",Combine(self.llm,self.tools).call_tool)
        self.graph_builder.add_node("apply_condition",condition)
        self.graph_builder.add_edge(START,"chatbot")
        self.graph_builder.add_conditional_edges("chatbot", # Source node
            condition, # The function that decides the next step
         { # If condition returns "chatbot", go to "chatbot"
            "tool_call": "call_tool", # If condition returns "tool_call", go to "call_tool"
            "end": END # Use END to signify graph termination)
         })
        self.graph_builder.add_edge("call_tool","chatbot")
        memory=MemorySaver()
        graph=self.graph_builder.compile(checkpointer=memory)
        config={"configurable":{"thread_id":"123"}}
        return graph.stream({"messages":HumanMessage(input)},config=config)
        