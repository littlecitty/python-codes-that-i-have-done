# 51. Handle file not found error.
 
try:
    with open("rough1.py", "r") as f:
        content = f.read()
        print(content)
except FileNotFoundError:
    print("Error: File not found!")



#pythonic
try: open("rough1asdlf.py")
except FileNotFoundError: print("file not found!")

