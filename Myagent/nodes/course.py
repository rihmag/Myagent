import httpx
from langchain.tools import tool
import logging
from typing import Dict, Any
import requests
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
class Course:
    def __init__(self):
        pass
    @tool
    def get_courses() -> Dict[str, Any]:
        """
        Gives out course details if a course-related query is asked.
        
        Returns:
            A dictionary containing the names and prices of all courses.
        """
        try:
            # Replace with your actual API URL
            api_url = "https://backend-1-bn9o.onrender.com//api/course/allcourses"
            
            # Add timeout and headers for better reliability
            headers = {
                'Accept': 'application/json',
                'User-Agent': 'CourseBot/1.0'
            }
            
            response = requests.get(api_url, headers=headers, timeout=30)
            response.raise_for_status()  # Raise an exception for bad status codes
            
            course_list = response.json()
            
            # Validate that we got a list
            if not isinstance(course_list, list):
                logger.error(f"Expected list but got {type(course_list)}")
                return {"error": "Invalid response format from API"}
            
            courses_info = []
            for item in course_list:
                if not isinstance(item, dict):
                    logger.warning(f"Skipping invalid item: {item}")
                    continue
                    
                title = item.get("title")
                price = item.get("price")
                
                if title and price:
                    courses_info.append({
                        "title": title,
                        "price": price
                    })
            
            if not courses_info:
                return {"message": "No courses found with valid title and price information"}
            print(courses_info)
            # Return structured data instead of concatenated strings
            return {
                "message": f"Here are the available courses:{courses_info}",
            }
            
        except requests.exceptions.RequestException as e:
            logger.error(f"API request failed: {e}")
            return {"error": f"Failed to fetch courses: {str(e)}"}
        except ValueError as e:
            logger.error(f"JSON parsing failed: {e}")
            return {"error": "Invalid JSON response from API"}
        except Exception as e:
            logger.error(f"Unexpected error: {e}")
            return {"error": f"An unexpected error occurred: {str(e)}"}