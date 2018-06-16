from threading import Thread,Condition
import threading
from .producer import Producer
import time
import requests
from requests.auth import HTTPBasicAuth
class Consumer(Thread):
    def __init__(self,p,c_id,s_id):
        self.producer=p
        self.c_id=c_id
        self.s_id=s_id

    def run(self):
        while(self.c_id not in self.producer.queue):
            time.sleep(1)
        self.producer.queue.pop(0)
        response=requests.get('http://127.0.0.1:8000/api/colleges/'+str(self.c_id)+'/students/'+str(self.s_id),auth=HTTPBasicAuth('saishankar','shankar123'))
        if response.status_code == 200:
            print("Thread id : ", threading.get_ident(), "Response Code : ", response.status_code, " : ", "Response : ",
                  response.text)
        else:
            print("Thread id : ", threading.get_ident(), "Response Code : ", response.status_code, " : ",
                  "Response : Invalid Response")
