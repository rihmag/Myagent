from states.state import State
class Condition():
    def __init__(self,llm):
        self.keywords=  ["support", "customer care", "help", "talk to agent", "contact support"]
        self.keywords_for_course=["course"]
        self.llm=llm
    def apply_condition(self, state: State) -> dict:
        response = self.llm.invoke(state["messages"])
        
        # Check if tool_calls exist in the response
        if response.tool_calls:
            # Check if any course-related keyword is in the messages
            if any(kw in state["messages"] for kw in self.keywords_for_course):
                return {"action": "course"}  # return as dict
            # Check if any other general keyword is in the messages
            elif any(kw in state["messages"] for kw in self.keywords):
                return {"action": "sendmail"}  # return as dict
        
        return {"action": "none"}  # default if no condition matches

                
