import os

print("==shell==")
while True:
    st = ""
    try:
        l = int(input("lines to exec:"))
    except Exception:
        print("must be int")
        l = 0
        
    
    for i in range(l):
        cm = input(">>>")
        st += cm
        st += "\n"
    try:
        os.system(st)
    except Exception as e:
        print(e)