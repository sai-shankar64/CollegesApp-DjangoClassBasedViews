import threading
import requests
from requests.auth import HTTPBasicAuth
def request(c_id,s_id):
    response=requests.get('http://127.0.0.1:8000/api/colleges/'+str(c_id)+'/students/'+str(s_id),auth=HTTPBasicAuth('saishankar','shankar123'))
    if response.status_code == 200:
        print("Thread id : ",threading.get_ident(),"Response Code : ",response.status_code," : ","Response : ",response.text)
    else:
        print("Thread id : ", threading.get_ident(), "Response Code : ", response.status_code, " : ", "Response : Invalid Response")
    return

if __name__ == "__main__":
    for i in range(32,50):
        t=threading.Thread(target=request,args=(1,i,))
        t.start()
        t.join()
    threading._main_thread
