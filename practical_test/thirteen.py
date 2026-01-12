class TransactionSystem:
    def __init__(self):
        self.data = {}       
        self.stack = []       

    def set(self, key, value):
        self.stack.append(self.data.copy())
        self.data[key] = value

    def commit(self):
        self.stack.clear()

    def rollback(self):
        if self.stack:
            self.data = self.stack.pop()

    def show(self):
        print(self.data)

t = TransactionSystem()

t.set("a", 10)
t.show()         

t.set("b", 20)
t.show()         

t.rollback()
t.show()        

t.set("c", 30)
t.show()        

t.commit()

