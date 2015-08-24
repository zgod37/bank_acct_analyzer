"""
Bank Account Anaylzer Main Program

A simple console interface to prompt user for command

Please see readme for details!
"""
import gen_line
import gen_stacked
import os

def display_menu():
    print("")
    print("------------ Main Menu ------------")
    print("Please Select Command")
    print("1 - Generate line graph of account balance over time")
    print("2 - Build stacked graph of amount spent per month at given locations")
    print("3 - Exit Program")

    return

def get_file_list():
    """
    Grab list of .txt files from accts folder
    """

    path_of_accounts = os.path.dirname(os.path.abspath(__file__)) + r"\accts"
    file_list = [path_of_accounts + '\\' + file_name for file_name in os.listdir(path_of_accounts) if file_name.lower().endswith('.txt')]

    return file_list

def display_line_graph():
    """
    Generates line graph of account balances over time
    """

    file_list = get_file_list()
    if file_list:
        print("found files:", file_list)
        choice = input("include totals? (Y/N) ")
        show_totals = 'True' if choice.upper() == 'Y' else False
        gen_line.generate_graph(file_list, show_totals)
    else:
        print("error: no files found! make sure your files are <acct_name>.txt")

    return

def display_stacked_graph():
    """
    Prompts user for an account and any number of locations and builds stacked bar graph
    """
    
    file_list = get_file_list()
    if file_list:
        print("")
        print("First choose one account from list")
        print("Files Found:")
        index = 1
        for file in file_list:
            print(index, "-", file)
            index += 1

        print("")
        print("Select account file to scan for locations")
        choice = int(input("Select File: "))
        if choice-1 < len(file_list) and choice > 0:
            acct_file = file_list[choice-1]
            print("you chose: ", acct_file)

            print("")
            print("now, type in any number of locations to see how much you're spending each month")
            print("IMPORTANT! please type each location separated by a space")
            print("e.g. if you want to know how much you're spending on groceries,")
            print("     you could type 'wal-mart kroger piggly-wiggly' etc!")
            print("")

            input_locations = input("Enter locations, separated by a space: ")
            if input_locations:
                locations = [word.upper() for word in input_locations.split(' ') if len(word) > 1]
                gen_stacked.generate_stacked_graph(acct_file, locations)
            else:
                print("no locations given!")
        else:
            print("invalid choice!")
    
    else:
        print("error: no files found! make sure your files are <acct_name>.txt!")

    return

def main():
    """
    Start main console interface
    """

    print("-------- Bank Account Analyzer --------")
    print("--------      by zgod          --------")
    print("")

    done = False
    while not done:
        display_menu()
        user_choice = input("Please enter choice: ")
        if user_choice == "1":
            display_line_graph()
        elif user_choice == "2":
            display_stacked_graph()
        elif user_choice == "3":
            done = True
        else:
            print("Invalid command!")

    return

main()




