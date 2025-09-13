# from states.state import State
import requests
from langchain.tools import tool
class Course:
    def __init__(self):
        pass
    @tool
    def get_courses(self):
        """
        gives out course details if course related query  is asked

        Returns:
           courses name and price
        """
        response = requests.get(
        "https://backend-1-bn9o.onrender.com/api/course/allcourses")
        list=response.json()
        for items in list:
            title=items.get("title")
            price=items.get("price")            
        return { "messages":f"title {title} price:{price}"} 
       
     
    

    
    
    

