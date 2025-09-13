from configparser import ConfigParser
class Config:
    def __init__(self):
        pass
    def get_llm_options(self):
        return "groq"
    def usecase_options(self):
        return ["Chatbot for  customers","chatbot for company"]
    def groq_options(self):
        return ["llama-3.1-8b-instant","llama-3.3-70b-versatile","openai/gpt-oss-20b"]
    def get_documents_options(self):
        return ["text","pdf"]
print("LOADED CONFIG")