# 48. Copy content of one file to another.
src=input("enter the source file path: ")
dst=input("enter the destination file path: ")

with open(src, 'r') as source_file:
    content=source_file.read()

with open(dst, 'w') as dest_file:
    dest_file.write(content)



#pythonic
with open(input("src: "), 'r') as s, open(input("dst: "), 'w') as d: d.write(s.read()) 
