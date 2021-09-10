import numpy as np
import time
class class1():
        Q=44

img=np.zeros([100,500,3], dtype=np.uint8) 
results = []

def getter(q, queue_return):
    global results
    while True:
     #   print("size of queue", q.qsize())
        item = q.get()
        print('getting item ...', item," size of queue:", q.qsize())
        if item is None:
            break
        time.sleep(0.4)
        results.append(755)
        queue_return.put(results) # Send back results


