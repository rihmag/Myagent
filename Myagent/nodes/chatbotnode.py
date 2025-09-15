from states.state import State
class node:
    def __init__(self,llm):
        self.llm=llm
    def call(self,state:State)-> dict:
        last_message = state['messages'][-1]
        print("this is the last message in chatbot node",last_message)
        messages=state["messages"]
        response=self.llm.invoke(messages)
        return {"messages":response}
        
        
        