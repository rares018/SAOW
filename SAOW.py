import os

print("==shell==")
while True:
    cmd = input(">>>")
    try:
        os.system(cmd)
    except Exception as e:
        print(e)