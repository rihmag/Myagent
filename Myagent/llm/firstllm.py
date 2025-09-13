from langchain_groq import ChatGroq


class Return_llm:
    def __init__(self,controls):
        self.user_controls=controls
        self.api_key=self.user_controls["GROQ_API_KEY"]
        
    def load(self):
        model=self.user_controls["selected_model"]
        llm=ChatGroq(api_key=self.api_key,model=model)
        return llm

        
