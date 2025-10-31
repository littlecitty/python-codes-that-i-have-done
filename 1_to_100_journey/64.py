# 64. Use `zip()` to combine lists.

class Combine:
    def __init__(self, names, age):
        self.names = names
        self.age = age

    def combine(self):
        return list(zip(self.names, self.age))

class UserOutp(Combine):
    def show_results(self):
        print("The combination of names & ages is:")
        for n, a in super().combine():
            print(f"{n} → {a} years old")

def user():
    names = tuple(x.strip() for x in input("Enter names separated with ',': ").split(','))
    age = tuple(map(int, input("Enter ages (respectively) separated with ',': ").split(',')))

    if len(names) != len(age):
        print("⚠️ Number of names and ages don’t match!")
        return

    obj = UserOutp(names, age)
    obj.show_results()

user()


