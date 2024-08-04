# this is a command line to do list program
import pyfiglet
from time import sleep
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
        new_item = input("what do you want to add\n")                
        with open("list.txt", "a") as file:
            file.write(f"\n{new_item}")
            while True:
                var = input("do you want to add a nother item? y/n\n").strip().lower()
                if var == "y":
                    break
                elif var == "n":
                    return
                else:
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

  #add fehler einfangen und if else zu ende schreiben 
 # nicht vergessen nummerrierung einzubauen
def main():
    ascii_art = pyfiglet.figlet_format("To-Do-List", font ="slant")
    print(ascii_art)
    print()
    print()
    print("welcome to the main menu of your to do list\n")
    sleep(2)
    print("what would you like to do?\n")
    print("""1. start a new list\n2. see whats on your to-do-list\n3. add to your to-do-list\n4. delete a completed task from your to-do-list\n5. quit""" )
    var = int(input("please press the corresponding number"))

if __name__ == "__main__":
   main()
