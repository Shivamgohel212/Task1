class MyDict:
    def __init__(self, data):
        self.data = data

    def get(self, key, default=None):
        for k in self.data:        
            if k == key:
                return self.data[k]
        return default             

d = MyDict({"name": "Amit", "age": 20})
print(d.get("name"))         
print(d.get("age"))           
print(d.get("marks"))         
print(d.get("marks", 0))      
