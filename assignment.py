import csv  # imports the csv module


def main():  # main function that controls entire program
    valid_choices = ["R", "C", "A", "M", "Q"]
    items_list = open_csv()

    user_choice = start_menu(items_list)  # calls the startup menu and checks what the user wants

    while user_choice != "Q":

        if user_choice == "R":
            required_items(items_list)  # calls the required items function

        elif user_choice == "C":
            completed_items(items_list)  # calls the completed items function

        else:
            print("Incorrect Input")

        user_choice = print_menu()

    print("USER CHOSE Q")


def open_csv():
    items = open('items.csv')
    csv_items = csv.reader(items)
    opened_list = list(csv_items)
    sum_items = len(items.readlines())
    return opened_list, items, sum_items


def start_menu(items_list):  # function for the startup menu
    print("Shopping List 1.0 - By Declan Evanson")
    total_csv_items = items_list[2]
    print("Successfully loaded {} items from {} \n".format(total_csv_items, items_list[1].name))
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
    for row in items_list[0]:
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
    for row in items_list[0]:
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
