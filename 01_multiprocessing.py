from multiprocessing import Process
import time

def brew(name):
    print(f"Started the {name} serving")
    time.sleep(3)
    print(f"{name} served !")

if __name__=="__main__":
    makers=[
        Process(target=brew,args=(f"Maker #{i+1}",)) 
        for i in range(3)
    ]

    #Start all process
    for p in makers:
        p.start()
    # Wail for all to complete
    for p in makers:
        p.join()
    
    print("All served !")