from multiprocessing import Process
import time

def cruch_number():
    print(f"Started the count process ")
    count=0

    for _ in range(100_000_000):
        count+=1
    print(f"Ended the count process")


if __name__=="__main__":

    start=time.time()

    p1=Process(target=cruch_number,name="Processor 1")
    p2=Process(target=cruch_number,name="Processor 2")

    p1.start()
    p2.start()
    p1.join()
    p2.join()

    end=time.time()

    print(f"Total time taken with multi processing is {end-start:.2f} seconds !")
