from threading import Thread, current_thread # import thread class

# create function contain thread
def display(n, msg):
    print("t1 thread details: " ,current_thread())
    for i in range(n):
        print(msg)
        
# creating new thread 
t1= Thread(target=display, kwargs={'n':5, 'msg' : 'hello world'}) 

# start the new thread
t1.start()