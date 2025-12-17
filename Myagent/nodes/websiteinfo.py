import httpx
from langchain.tools import tool
import logging
from typing import Dict, Any
import requests
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
class WebsiteInfo:
    def __init__(self):
        pass
    @tool
    def get_website_info()->str:
        """
        Gives out course details if a website related or platform related  query is asked.
        
        Returns:
            A text containing website description and what the platform does.
        """
        return "this the main website of yr-elearning platform part of yr it solutions enterprise expansion of yr it solutions we provide educational content , for further details for building with us website link is https://yrit-solutions.vercel.app"
            # Replace with your actual API URL
           
            
           