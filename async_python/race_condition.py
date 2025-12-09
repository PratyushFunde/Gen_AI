import threading

counter=0

def reset():
    global counter
    for _ in range(100_000):
        counter+=1

threads=[threading.Thread(target=reset) for _ in range(2)]

[t.start() for t in threads]
[t.join() for t in threads]

print(f"Count is : {counter}")