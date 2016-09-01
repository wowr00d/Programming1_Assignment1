import csv  # imports the csv module

def main():  # main function that controls entire program
    valid_choices = ["R","C","A","M","Q"]
    items = open('items.csv')
    csv_items = csv.reader(items)
    items_list = list(csv_items)
    print(items_list)

    user_choice = start_menu(csv_items,items)

    while user_choice not in valid_choices:
        print("Incorrect Input")
        print_menu()

    if user_choice == "R":
        required_items(items_list) # calls the required items function

def start_menu(cvs_items,items):
    print("Shopping List 1.0 - By Declan Evanson")
    total_csv_items = len(items.readlines())
    print("Successfully loaded {} items from {} \n".format(total_csv_items, items.name))
    print("Menu: \n" + "R - List Required Items \n" + "C - List Completed Items \n" + "A - Add New Items \n" + "M - Mark as completed \n" + "Q - Quit \n")
    choice = (input("Enter your choice: "))
    choice = choice.upper()
    return choice

def print_menu():
    print("Menu: \n" + "R - List Required Items \n" + "C - List Completed Items \n" + "A - Add New Items \n" + "M - Mark as completed \n" + "Q - Quit \n")
    choice = input("Enter your choice: ")
    return choice

def required_items(items_list):
    print("List required Items")
    price_totals = 0
    row_total = 0
    for row in items_list:
        if "r" in row:
            row[1] = float(row[1])
            row[2] = int(row[2])
            
            print(row_total, row[0], "$ ", row[1], row[2])
            price_totals += row[1]
            row_total += 1

    print("Total price of {} items is $ {}".format(row_total,price_totals))





main()