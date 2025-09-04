# Keep asking for input until the user types 'done'

while True:
    name = input("Enter your name (or type 'done' to finish): ")      # input name
    
    if name == "done":
        break               # exit loop if user types 'done'
    else:
        print("Hello, " + name + "!")   # greet the user