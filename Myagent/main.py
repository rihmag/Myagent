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
    print("this is the result",result)
    for items in result:
        print("this is the items in the result",items)
        if items.get("chatbot"):
            st.write(items.get("chatbot")['messages'].content)
        if items.get("call_tool"):
            st.write(items.get("call_tool")['messages'])
        if items.get("get_courses"):
            st.write(items.get("get_courses"))
        if items.get("sendmail"):
            st.write(items.get("sendmail")['messages'])
        if items.get("get_user_query"):
            st.write(items.get("get_user_query")['messages'])
    
    
    
