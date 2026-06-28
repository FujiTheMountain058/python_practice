import time

def type(msg):
    for write in msg: 
        print(write, end="", flush=True)
        time.sleep(.05)
    print()

type("Programming is the process of creating a set of detailed, step-by-step instructions that tell a computer how to perform a task or solve a specific problem. It involves designing algorithms and writing code using programming languages (like Python, JavaScript, or C++) that the machine can execute")