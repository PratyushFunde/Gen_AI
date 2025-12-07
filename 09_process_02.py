from multiprocessing import Process
import time

def cpu_heavy():
    print(f"Crunchin some numbers.")
    total=0
    for i in range(10**8):
        total+=1
    print("Done crunching!")

if __name__=="__main__":

    start=time.time()
    
    processes=[Process(target=cpu_heavy) for _ in range(2)]
    [t.start() for t in processes]
    [t.join() for t in processes]
    
    end=time.time()
    
    print(f"Time taken to complete is {end-start:2f} seconds")