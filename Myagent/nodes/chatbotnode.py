from states.state import State
class node:
    def __init__(self,llm):
        self.llm=llm
    def call(self,state:State)-> dict:
        messages=state["messages"]
        response=self.llm.invoke(messages)
        return {"messages":response}
        
        
        