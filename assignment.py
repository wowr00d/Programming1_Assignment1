import csv  # imports the csv module
import operator

FILE_NAME = 'items.csv'

def main():  # main function that controls entire program
    valid_choices = ["R", "C", "A", "M", "Q"]
    items_list = open_csv()

    user_choice = start_menu(items_list)  # calls the startup menu and checks what the user wants

    while user_choice != "Q":

        if user_choice == "R":
            required_items(items_list)  # calls the required items function

        elif user_choice == "C":
            completed_items(items_list)  # calls the completed items function

        elif user_choice == "M":
            mark_items(items_list)  # calls the completed items function

        else:
            print("Incorrect Input")

        user_choice = print_menu()

    print("USER CHOSE Q")


def open_csv():
    items_file = open('items.csv')
    reader = csv.reader(items_file)
    items = list(reader)
    for item in items:
        item[1] = float(item[1])
        item[2] = int(item[2])

    items_file.close()
    items.sort(key=operator.itemgetter(2))
    return items


def mark_items(items_list):
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
        change_item = input("Choose number you wish to change")
        change_item = int(change_item)
        for row in items_list:
            if change_item in row:
                row[3] = 'c'
                print(items_list)

def start_menu(items_list):  # function for the startup menu
    print("Shopping List 1.0 - By Declan Evanson")
    print("Successfully loaded {} items from {} \n".format(len(items_list), 'items.csv'))
    print(
        "Menu: \n" + "R - List Required Items \n" + "C - List Completed Items \n" + "A - Add New Items \n" + "M - Mark as completed \n" + "Q - Quit \n")
    choice = (input("Enter your choice: "))
    choice = choice.upper()
    return choice


def print_menu():  # function for the menu that is displayed after initial startup
    print(
        "Menu: \n" + "R - List Required Items \n" + "C - List Completed Items \n" + "A - Add New Items \n" + "M - Mark as completed \n" + "Q - Quit \n")
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
        print("Total price of {} item/s is $ {} \n".format(row_total, price_totals))

    return


main()
