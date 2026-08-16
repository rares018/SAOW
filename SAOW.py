import os
print("==shell== |q to exit")
while True:
    cmd = input(">>>")
    if cmd == "quit" or cmd == "q":
        break
    else:
        try:
            os.system(cmd)
        except KeyboardInterrupt:
            pass
        except Exception as e:
            print(e)