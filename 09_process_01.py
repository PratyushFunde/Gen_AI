import threading
import time

def cpu_heavy():
    print(f"Crunchin some numbers.")
    total=0
    for i in range(10**8):
        total+=1
    print("Done crunching!")

start=time.time()

threads=[threading.Thread(target=cpu_heavy) for _ in range(4)]
[t.start() for t in threads]
[t.join() for t in threads]

end=time.time()

print(f"Time taken to complete is {end-start:2f} seconds")