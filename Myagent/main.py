from ui.loadui import LoadUI
import streamlit as st
from llm.firstllm import Return_llm
from graphs.firstgraph import FirstGraph
from nodes.course import Course
from nodes.sendmail import SendMail
user_input=LoadUI()
input = user_input.load_ui()
user_controls=input[0]
chat_input=input[1]
if not input[0] and not input [1]:
    st.error("complete the user input ")

else: 
    return_llm=Return_llm(controls=user_controls)
    llm=return_llm.load()
    first_graph=FirstGraph(llm=llm)
    str=str(chat_input)
    result=first_graph.graph(input=str)
    print(result)
    st.write(result)
    
    
    
