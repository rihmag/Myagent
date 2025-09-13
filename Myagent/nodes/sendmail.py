from states.state import State
from langchain.tools import tool
class SendMail:
    def __init__(self):
        pass
    @tool
    def sendmail()->dict:
        """_summary_
                sends mail to the customer care of company
        Args:
           takes the messages state as arguments 

        Returns:
            confirmation of email has been sent to customer care
        """
        return {"messages":{"i have send mail to this email address"}}