from onlineapp.ClientThreads import *
import random
if __name__=="__main__":
    p=Producer()
    for i in range(32,44):
        c=Consumer(p,1,i)
        c.start()

