# 49. Rename a file using `os` module.
import os

try:
    old_name = input("Enter the current file path: ")
    new_name = input("Enter the new file path: ")
    
    os.rename(old_name, new_name)
    print("✅ File renamed successfully!")

except FileNotFoundError:
    print("❌ The file you want to rename was not found.")
except PermissionError:
    print("❌ You don't have permission to rename this file.")
except Exception as e:
    print(f"⚠️ Error: {e}")



#pythoic
import os; import sys; old=input("Old path: "); new=input("New path: "); (os.rename(old, new), print("✅ Renamed!")) if os.path.exists(old) else print("❌ File not found!") or sys.exit()

