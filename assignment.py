import csv  # imports the csv module


def main():  # main function that controls entire program
    print('{:>15}'.format('centered'))
    valid_choices = ["R", "C", "A", "M", "Q"]
    items = open('items.csv')
    csv_items = csv.reader(items)
    items_list = list(csv_items)
    print(items_list)

    user_choice = start_menu(csv_items, items)  # calls the startup menu and checks what the user wants

    while user_choice != "Q":

        if user_choice == "R":
                required_items(items_list)  # calls the required items function

        elif user_choice == "C":
                completed_items(items_list)  # calls the completed items function

        else:
            print("Incorrect Input")

        user_choice = print_menu()

    print("USER CHOSE Q")

def start_menu(cvs_items, items):  # function for the startup menu
    print("Shopping List 1.0 - By Declan Evanson")
    total_csv_items = len(items.readlines())
    print("Successfully loaded {} items from {} \n".format(total_csv_items, items.name))
    print(
        "Menu: \n" + "R - List Required Items \n" + "C - List Completed Items \n" + "A - Add New Items \n" + "M - Mark as completed \n" + "Q - Quit \n")
    choice = (input("Enter your choice: "))
    choice = choice.upper()
    return choice


def print_menu():  # function for the menu that is displayed after initial startup
    print("Menu: \n" + "R - List Required Items \n" + "C - List Completed Items \n" + "A - Add New Items \n" + "M - Mark as completed \n" + "Q - Quit \n")
    choice = input("Enter your choice: ")
    choice = choice.upper()
    return choice


def required_items(items_list):  # function for the check required items option
    print("List required Items: \n")
    price_totals = 0
    row_total = 0
    for row in items_list:
        if "r" in row:
            row[1] = float(row[1])
            row[2] = int(row[2])
            print("{} {} ${} {}".format(row_total, row[0], row[1], row[2]))
            price_totals += row[1]
            row_total += 1
    if price_totals == 0:  # a check to see if there are actually any required items
        print("No required items")
    else:
        print("Total price of {} item/s is ${} \n".format(row_total, price_totals))

    return

def completed_items(items_list):  # function for the check completed items options
    print("List completed Items: \n")
    price_totals = 0
    row_total = 0
    for row in items_list:
        if "c" in row:
            row[1] = float(row[1])
            row[2] = int(row[2])
            print(row_total, row[0], "$ ", row[1], row[2])
            price_totals += row[1]
            row_total += 1
    if price_totals == 0:  # a check to see if there are actually any completed items
        print("No completed items")
    else:
        print("Total price of {} item/s is $ {}".format(row_total, price_totals))

    return


main()
