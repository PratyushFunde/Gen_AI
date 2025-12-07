import threading
import time

def makeDrink(type_,wait_time):
    print(f"Making {type_} brewing...")
    time.sleep(wait_time)
    print(f"{type_} ready")

t1=threading.Thread(target=makeDrink,args=("Masala",2))
t2=threading.Thread(target=makeDrink,args=("Ginger",3))

t1.start()
t2.start()

t1.join()
t2.join()

print("All done !")

