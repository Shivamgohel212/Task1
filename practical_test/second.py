class color:
    def red(self):
        return True

    def yellow(self, value):
        return value is False
obj = color()
if obj.red():
    print("True")
print(obj.yellow(False))
print(obj is False)