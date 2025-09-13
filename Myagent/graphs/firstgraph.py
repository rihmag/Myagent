from states.state import State
from langgraph.graph import StateGraph,START,END
from llm.firstllm import Return_llm
from langchain_core.messages import HumanMessage
from nodes.chatbotnode import node
from nodes.sendmail import SendMail
from nodes.condition import Condition
from nodes.course import Course
from langgraph.checkpoint.memory import MemorySaver
memory=MemorySaver()
class FirstGraph:
    def __init__(self,llm):
        self.graph_builder=StateGraph(State)
        self.llm=llm
        
    def graph(self,input):
        self.graph_builder.add_node("chatbot", node(self.llm).call)
        self.graph_builder.add_node("get_courses",Course.get_courses)
        condition=Condition(self.llm)
        self.graph_builder.add_node("apply_condition",condition.apply_condition(state=))
        self.graph_builder.add_node("sendmail",SendMail.sendmail)
        self.graph_builder.add_edge(START,"chatbot")
        self.graph_builder.add_conditional_edges("apply_condition","get_courses")
        self.graph_builder.add_edge("apply_condition","sendmail")
        self.graph_builder.add_edge("get_courses",END)
        self.graph_builder.add_edge("sendmail",END)
        memory=MemorySaver()
        graph=self.graph_builder.compile(checkpointer=memory)
        config={"configurable":{"thread_id":"123"}}
        return graph.stream({"messages":HumanMessage(input)},config=config)
        