# this is a command line to do list program
import pyfiglet
from time import sleep
# creates a new, empty todo list with headline 'to-do-list'
def create_new_list():
    with open("list.txt", "w") as file:
        file.write("To-Do-List")        #todo fix problem with index 

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
                file.write(f"{index}. {line}")              #todo fix problem with index 



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
    print("welcome to the main menu of your to do list\n")
    sleep(2)
    print("what would you like to do?\n")
    while True:
        print("""1. start a new list\n2. see whats on your to-do-list\n3. add to your to-do-list\n4. delete a completed task from your to-do-list\n5. quit""" )
        try:
            var = int(input("please press the corresponding number"))
            if var == 1:
                create_new_list()   #creates a new list
                add_item()          #lets user add tasks 
                delete_number()     #cleans the numeration in case user put wrong numbers 
                number_tasks()      #correctly numbers the tasks
            elif var == 2:
                open_list()
                print()
                print("would you like to add or delete something?")
                print()
            else:
                if var == 3:
                    add_item()
                    delete_number()
                    number_tasks()
                    print("this is your new to-do-list")
                    print()
                    open_list()
                    print()
                elif var == 4:  #todo Handle input errors:
                    open_list()
                    lines_to_delete_input = input("Please enter the numbers of the tasks you'd like to delete, separated by a comma: ") #gets user input as string
                    lines_to_delete = [int(x.strip()) for x in lines_to_delete_input.split(",") if x.strip().isdigit()] # cuts the string by the','s converts it to int and saves it in a list all in one line very cool!
                    delete_lines("list.txt", lines_to_delete)
                    delete_number()
                    number_tasks()
                    print("This is your new to-do-list:")
                    open_list()
                    print()
                else:
                    if var == 5:
                        exit()
                    else:
                        print("please use the designated numbers to indicate your choice")
        except ValueError:
            print("please use the designated numbers to indicate your choice")

            
            

if __name__ == "__main__":
   main()
