import datetime
def greetings(name):
    current_time=datetime.time()
    if current_time<datetime.time(12,0):
        return "Hello! Good Morning!"
    elif current_time<datetime.time(17,0):
        return "Hello! Good afternoon!"
    else:
        return "Hello! Good Evening!"

name=input("Enter your name: ")
greet=greetings(name)
print(greet,name)