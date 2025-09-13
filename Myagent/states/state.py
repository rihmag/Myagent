from typing import TypedDict,Annotated
from langgraph.graph import add_messages
from langchain_core.messages import AnyMessage
class State(TypedDict):
    messages:Annotated[list[AnyMessage],add_messages]
    
