
--------------------15
class Event:
    def __init__(self):
        self.handlers = []

    def subscribe(self, func):
        self.handlers.append(func)

    def trigger(self):
        for handler in self.handlers:
            try:
                handler()
            except Exception as e:
                print("Error ignored:", e)


# Handlers (functions)
def handler_one():
    print("Handler One executed")

def handler_two():
    print("Handler Two executed")
    raise ValueError("Something went wrong")

def handler_three():
    print("Handler Three executed")


# Using the event system
event = Event()

event.subscribe(handler_one)
event.subscribe(handler_two)
event.subscribe(handler_three)

event.trigger()

