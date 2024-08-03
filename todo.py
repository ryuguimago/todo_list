# this is a command line to do list program

# creates a new, empty todo list with headline 'to-do-list'
def create_new():
    with open("list.txt", "w") as file:
        file.write("To-Do-List")

# opens the existing list and displays its content
def open_list():
    with open('list.txt', 'r') as file:
        content = file.read()
        print(content)

# takes user input and saves it to the existing list
def add_item():
    new_item = input("what do you want to add\n")
    with open("list.txt", "a") as file:
        file.write(f"\n{new_item}")


