# this is a command line to do list program
import pyfiglet
from time import sleep
from termcolor import colored, cprint
# creates a new, empty todo list with headline 'to-do-list'
def create_new_list():
    with open("list.txt", "w") as file:
        file.write("To-Do-List")         

# opens the existing list and displays its content
def open_list():
   with open('list.txt', 'r') as file:
    for line in file:
        cprint(line.strip(), "magenta")
        
    


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
                    return          #returns to main function
                else:
                    cprint("please use 'y' or 'n' to indicate your choice", "red")
                         
              



# deletes old numbers of tasks
def delete_number():
    with open("list.txt", "r") as file:
        lines =file.readlines()
        with open("list.txt", "w") as file:
            for line in lines:
                parts = line.split(". ", 1) #splits the lines after the first '. ' to seperate the number from the task. the space behind the'.' is importend
                if len(parts) > 1 and parts[0].strip().isdigit():   # checks if the line was numbered
                    clean = parts[1]   #saves only the part after the '.'
                else:
                    clean = line # keeps unnumbered lines e.g. headline
                file.write(clean)   #writes the clean line back

# numbers the tasks based on position in list
def number_tasks():
    with open("list.txt", "r") as file:
        lines =file.readlines()
        
        # writes back numbered tasks
        with open("list.txt", "w") as file:
            if lines:
                file.write(lines[0]) # write first line without number
                for index, line in enumerate(lines[1:], start=1): # start numbering
                    file.write(f"{index}. {line}")              
           


# deletes specific lines from list
def delete_lines(filename, lines_to_delete):
    # open file
    with open("list.txt", "r") as file:
        lines = file.readlines()
    # write back only lines not to be deleted 
    with open("list.txt", "w") as file:
        for index, line in enumerate(lines):   #iterates through lines
            if index not in lines_to_delete:            #writes whats not in the lines_to_delete list
                file.write(line)

def main():
    ascii_art = pyfiglet.figlet_format("To-Do-List", font ="slant")
    print(ascii_art)
    print()
    print()
    sleep(2)
    while True:
        cprint("""      MENU\n1. start a new list\n2. see whats on your to-do-list\n3. add to your to-do-list\n4. delete a completed task from your to-do-list\n5. quit""", "yellow" )
        try:
            var = int(input("please press the corresponding number\n"))
            if var == 1:
                create_new_list()   #creates a new list
                add_item()          #lets user add tasks 
                delete_number()     #cleans the numeration in case user put wrong numbers 
                number_tasks()      #correctly numbers the tasks
            elif var == 2:
                try:
                    open_list()
                    print()
                    cprint("would you like to add or delete something?", "green")
                    print()
                except FileNotFoundError:
                    cprint("you dont have a to-do-list yet", "red")
                    print()
            elif var == 3:
                    add_item()
                    delete_number()
                    number_tasks()
                    cprint("this is your new to-do-list", "green")
                    print()
                    open_list()
                    print()
            elif var == 4:  #todo Handle input errors:
                    open_list()
                    lines_to_delete_input = input("Please enter the numbers of the tasks you'd like to delete, separated by a comma: ") #gets user input as string
                    try:
                        lines_to_delete = [int(x.strip()) for x in lines_to_delete_input.split(",") if x.strip().isdigit()] # cuts the string by the','s converts it to int and saves it in a list all in one line very cool!
                        delete_lines("list.txt", lines_to_delete)
                        delete_number()
                        number_tasks()
                        cprint("This is your new to-do-list:", "green")
                        open_list()
                        print()
                    except ValueError:          #wird meiner ansicht nach nicht getriggert muss bessere methode geben
                        cprint("please enter the numbers of the task you'd like to delete, seperated by commas: ", "red")
            elif var == 5:
                    exit()
            else:
                cprint("please use the designated numbers to indicate your choice", "red")
        except ValueError:
            cprint("please use the designated numbers to indicate your choice", "red")

            
            

if __name__ == "__main__":
   main()
