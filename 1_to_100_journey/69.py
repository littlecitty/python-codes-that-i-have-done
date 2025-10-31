# 69. Find all duplicates in a list.

class Duplicates:
    def __init__(self, combi):
        self.combi = combi

    def cal(self):
        seen = set()
        duplicates = set()
        for item in self.combi:
            if item in seen:
                duplicates.add(item)
            else:
                seen.add(item)

        print("Duplicates:", list(duplicates) if duplicates else "None")

def User():
    combi = input("Enter list of names like: a,b,c : ").split(',')
    obj = Duplicates(combi)
    obj.cal()

User()

