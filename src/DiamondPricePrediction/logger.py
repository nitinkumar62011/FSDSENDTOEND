import logging
import os
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
log_path=os.path.join(os.getcwd(),"logs")
os.makedirs(log_path,exist_ok=True)
LOG_FILE_PATH=os.path.join(log_path,LOG_FILE)
logging.basicConfig(level=logging.INFO,
                    filename=LOG_FILE_PATH,
                    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s -- %(message)s"
                    
                    )
# class Logger:
#     def __init__(self):
#         self.LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
#         self.log_path=os.path.join(os.getcwd(),"logs")
#         os.makedirs(self.log_path,exist_ok=True)
#         self.LOG_FILE_PATH=os.path.join(self.log_path,self.LOG_FILE)
        
    
    
#     def loggerMethod(self,mess):
#         logging.basicConfig(level=logging.INFO,
#                     filename=self.LOG_FILE_PATH,
#                     format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s -- %(message)s"
                    
#                     )
#         logging.info(mess)
        
    