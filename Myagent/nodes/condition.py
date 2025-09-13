from states.state import State
class Condition():
    def __init__(self,llm):
        self.keywords=  ["support", "customer care", "help", "talk to agent", "contact support"]
        self.keywords_for_course=["course","courses"]
        self.llm=llm
    def apply_condition(self, state:State):
        last_message = state['messages'][-1]
        print("this is the last message in apply_condition",last_message)
        # print("this is the last message in condition",last_message.additional_kwargs.get("tool_calls")[0])
        # Check for keywords in the last user message 
        if last_message.additional_kwargs.get("tool_calls"):
            return "tool_call"

        
        
        # Check if tool_calls exist in the response
        
            
        
    
        
        return "end" # default if no condition matches

                
