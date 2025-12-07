import threading
import time

def brew():
    print(f"{threading.current_thread().name} started brewing...")
    count=0

    for i in range(100_000_000):
        count+=1
    print(f"{threading.current_thread().name} finidshed brewing !")

t1=threading.Thread(target=brew,name="B1")
t2=threading.Thread(target=brew,name="B2")

start=time.time()
t1.start()
t2.start()

t1.join()
t2.join()

end=time.time()

print(f"Total time taken = {end-start:.2f} seconds")