# 45. Read a file and count lines.
# Ask for the file path
file_path = input("Enter file path: ")

# Open and read file
with open(file_path, 'r') as file:
    line_count = sum(1 for _ in file)  # Counts each line

print(f"Total number of lines: {line_count}")



#pythonic
print(len(open(input("Enter file path: ")).read().splitlines()))

