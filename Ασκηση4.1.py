'''
Python Mini Project Ασκηση 4.1
'''
import time
dic={}
while True:
    text = input("ΑΜ, Όνομα:")
    if text=="q":
        break
    else:
        data=text.split(", ")
        data[0]=int(data[0])
        dic[data[0]]=data[1]


for x in sorted(dic):
        print(x, dic[x])


time.sleep(10)
