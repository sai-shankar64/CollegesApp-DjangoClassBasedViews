from threading import Thread
import random
import time
class Producer(Thread):
    def __init__(self):
        self.queue=[]

    def run(self):
        for i in range(10):
            rand=random.randint(1,22)
            while(rand in self.queue):
                rand = random.randint(1, 22)
            self.queue.append(rand)
            time.sleep(2)

