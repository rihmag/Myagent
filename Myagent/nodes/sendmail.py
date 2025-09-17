import smtplib
from states.state import State
from langchain.tools import tool
import os
from dotenv import load_dotenv
import streamlit as st
load_dotenv()
class SendMail:
    def __init__(self):
        pass
    @tool
    def get_user_query()->dict:
        """_summary_
            gets user query from state messages
        Args:
            no args taken just returns prompt instructions to user
        Returns:
            confirmation of user query has been received
        """
        return {"messages":{"please enter the following details name:your_name,email:your_email_address,query:your_course_related_query"}}

    @tool
    def sendmail(name:str,email:str,query:str)->dict:
        """
        Sends mail to the customer care of the company.

        Args:
            name (str): Name of the user.
            email (str): User's email address.
            query (str): The user's query.

        Returns:
            dict: Confirmation that the email has been sent.
        """
        destination_email="gambhiranant002@gmail.com"
        sender_email="dominictorretof10@gmail.com"
        message=query
        subject="this regarding a student query related to your course by name "+name+" and email address "+email
        text = f"Subject: {subject}\n\n{message}"
        server=smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        server.login(sender_email,st.secrets["app_password"])
        server.sendmail(sender_email,destination_email,text)
        print("email has been sent")
        return {"messages":{"your query has been registered, they will reach out to you soon"}}
