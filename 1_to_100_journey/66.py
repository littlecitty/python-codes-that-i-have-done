# 66. Dictionary comprehension to swap keys and values.

class Exchange:
    def __init__(self, **kwargs):
        self.kwargs = kwargs

    def exch(self):
        # Swap keys and values using dictionary comprehension
        return {v: k for k, v in self.kwargs.items()}


class VaKeys(Exchange):
    def OutputValue(self):
        print(f"The Dictionary comprehension to swap keys and values is: {self.exch()}")


def user():
    # Convert input string into a dictionary
    kwargs = {k: v for k, v in (item.split('=') for item in input("Enter name=abc,age=10: ").split(','))}
    
    obj = VaKeys(**kwargs)
    obj.OutputValue()


user()

