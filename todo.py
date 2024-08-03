# this is a command line to do list program
import pyfiglet
# creates a new, empty todo list with headline 'to-do-list'
def create_new_list():
    with open("list.txt", "w") as file:
        file.write("To-Do-List")

# opens the existing list and displays its content
def open_list():
   with open('list.txt', 'r') as file:
    while True:
        line = file.readline()
        if not line:
            break
        print(line.strip())
        
    


# takes user input and saves it to the existing list
def add_item():
    while True:
        new_item = input("what do you want to add\n")                   #ausnahmen einfangen und error handling noch einfügen
        with open("list.txt", "a") as file:
            file.write(f"\n{new_item}")
            try:
                var = input("do you want to add a nother item? y/n\n").strip().lower()
                if var == "n":
                    break
            except ValueError:
                print("please use 'y' or 'n' to indicate your choice")



# deletes old numbers of tasks
def delete_number():
    with open("list.txt", "r") as file:
        lines =file.readlines()
        with open("list.txt", "w") as file:
            for line in lines:
                parts = line.split(".")
                clean = parts[-1]
                file.write(clean)
# numbers the tasks based on position in list
def number_tasks():
    with open("list.txt", "r") as file:
        lines =file.readlines()
        # writes back numbered tasks
        with open("list.txt", "w") as file:
            for index, line in enumerate(lines, start=1):
                file.write(f"{index}. {line}")



# deletes specific lines from list
def delete_lines(filename, lines_to_delete):
    # open file
    with open("list.txt", "r") as file:
        lines = file.readlines()
    # write back only lines not to be deleted 
    with open("list.txt", "w") as file:
        for index, line in enumerate(lines, start=1):
            if index not in lines_to_delete:
                file.write(line)


def main():
    ascii_art = pyfiglet.figlet_format("To-Do-List", font ="slant")
    print(ascii_art)
    print()
    print()
    print("Do You Want to Start a New To-Do-List or Acces an Existing One?")
    while True:                         #add fehler einfangen und if else zu ende schreiben 
                                        # nicht vergessen nummerrierung einzubauen
        var = input("please enter 'new' for a new list or 'old' for an existing list").strip().lower()
        if var == "new":
            create_new_list()
            add_item()


if __name__ == "__main__":
    main()
