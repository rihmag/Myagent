import streamlit as st
import os
from dotenv import load_dotenv
load_dotenv()
from  ui.uiconfig import Config
os.environ["GROQ_API_KEY"]=os.getenv("GROQ_API_KEY")
class LoadUI:
    def __init__(self):
        self.config=Config()
        self.user_controls={}
        self.query=str
    def load_ui(self):
        st.title("Yr it Assistant ")
        st.subheader("an AI-powered chatbot to assist you with your course-related queries")
        
        documents_option=self.config.get_documents_options()
        use_case_options=self.config.usecase_options()
        groq_options=self.config.groq_options()
        usecase=st.selectbox("choose chatbot",use_case_options)
        col1,col2=st.columns(2)
       
        with col1:
          
            chosen=st.selectbox("select the brain",groq_options)
            st.write("you chose",chosen)
        with col2:
            st.write("")
            st.write("")
            self.query =st.chat_input("enter the text")
           
           
        select_type_of_documents=st.sidebar.selectbox(" ",documents_option)
        add_documents=st.sidebar.file_uploader("add documents",type=select_type_of_documents)
        self.user_controls["selected_model"]=chosen
        self.user_controls["GROQ_API_KEY"]=os.getenv("GROQ_API_KEY")
        self.user_controls["usecases"]=use_case_options
        
        if add_documents:
            st.write("your documents has been uploaded")
        
        return [self.user_controls,self.query]


    