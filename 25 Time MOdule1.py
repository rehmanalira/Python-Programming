"""
Time module is properity which we use in diffrent
sections we can use it to get the diffrence between two things that
how much it takes the tim

"""
import time
t=time.time()#it is a initail time
i=0
while(i<200):
    print("RA")
    i+=1
print(f"time taken is{time.time()-t}")#here we - the initail time
#to how much time it takes
t2=time.time()
for j in range(200):
    #time.sleep(1)#it will print the number after 1 second
    print("RA JUtt")
print("Time taken is",time.time()-t2)

"""mytime=time.asctime(time.time())
print("NOw time is",mytime)"""