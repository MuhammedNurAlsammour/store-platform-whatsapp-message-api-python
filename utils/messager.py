import pywhatkit
import time
from datetime import datetime

class Messager():
  def __init__(self):pass

  def send(self, phone:str, message:str, waitTime: int):
      """
      Send WhatsApp text message endpoint
      """
      pywhatkit.sendwhatmsg_instantly(
                    phone_no=phone,
                    message=message,
                    wait_time=waitTime,
                )