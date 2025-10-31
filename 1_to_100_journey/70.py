#70. Check if a string is a valid identifier.

import keyword

class Identifier:
    def __init__(self, string_):
        self.string_ = string_

    def cal(self):
        s = self.string_
        if s.isidentifier() and not keyword.iskeyword(s):
            print("Valid identifier")
        else:
            print("Not valid identifier")

def User():
    char = input("Enter string: ")
    obj = Identifier(char)
    obj.cal()

User()

#imporoved version
import re

class Identifier:
    def __init__(self, string_):
        self.string_ = string_

    def cal(self):
        s = self.string_
        if re.fullmatch(r'[A-Za-z_][A-Za-z0-9_]*', s):
            print("Valid identifier (but not checking keywords)")
        else:
            print("Not valid identifier")

def User():
    char = input("Enter string: ")
    obj = Identifier(char)
    obj.cal()

User()

