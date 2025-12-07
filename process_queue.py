from multiprocessing import Queue,Process,Value

def prepare(queue):
    queue.put("Masala is ready.")

counter=Value('i',0)

queue=Queue()

if __name__=="__main__":

    p=Process(target=prepare,args=(queue,))
    p.start()
    p.join()
    print(queue.get())