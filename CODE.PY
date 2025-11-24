from time import *
import random as r
print(time())
def mistake(paragraph_test,usertest):
    error=0
    for i in range(len(paragraph_test)):
        try:
            if pargraph_test[i]!=usertest[i]:
                error=error+1
        except:
            error=error+1
    return error
def speed_time(time_s,time_e,userinput):
    time_delay=time_e-time_s
    time_R=round(time_delay,2)
    speed=len(userinput)/time_R
    return round(speed)
while True:
    ck=input("are you ready to test:yes/no:")
    if ck=="yes":
       test=["An array is a data structure that stores a collection of elements of the same data type in contiguous memory locations.","Each element is identified by a unique numerical index, which represents its position in the array, starting from 0","whereas a list is an ordered, mutable data structure that stores a collection of items, which can include different data types.", " Lists are fundamental for organizing data, as they maintain the order of elements, allow duplicates, and can be modified after creation."]
       test1=r.choice(test)
       print("*******typing speed calculator*********")
       print(test1)
       print()
       print()
       time_1=time()
       test_input=input("enter:")
       time_2=time()
       print("speed :",speed_time(time_1,time_2,test_input),"w/sec")
       print("error:",mistake(test1,test_input))
    elif ck =="no":
        print("thank you")
        break
    else:
        print("wrong input")
    
