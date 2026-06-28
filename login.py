import time 

USERNAME = input("USERNAME: ")
PASSWORD = input("PASSWORD: ")

if USERNAME == "User1" and PASSWORD == "1234":
    print("CHECKING INPUT...")
    time.sleep(2)
    print("LOGIN SUCCESS WELCOME BACK", USERNAME.upper())
else:
    print("CHECKING INPUT...")
    time.sleep(2)
    print("ERROR: INVALID USERNAME OR PASSWORD")