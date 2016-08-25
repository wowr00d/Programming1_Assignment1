import csv

def main():
    valid_choices = ["R","C","A","M","Q"]
    f = open('items.csv')
    csv_f = csv.reader(f)
    
    print("Shopping List 1.0 - By Declan Evanson")
    total_csv_items = len(f.readlines())
    print("Successfully loaded {} items from {}".format(total_csv_items, f.name))

    print("Menu: \n" + "R - List Required Items \n" + "C - List Completed Items \n" + "A - Add New Items \n" + "M - Mark as completed \n" + "Q - Quit \n")
    user_choice = (input("Enter your choice: "))
    user_choice = user_choice.upper()

    while user_choice not in valid_choices:
        print("Incorrect Input")
        print("Menu: \n" + "R - List Required Items \n" + "C - List Completed Items \n" + "A - Add New Items \n" + "M - Mark as completed \n" + "Q - Quit \n")
        user_choice = input("Enter your choice: ")

    if user_choice == "R":
        print("List required Items")
        f = open('items.csv')
        csv_f = csv.reader(f)
        for row in csv_f:
            if "r" in row:
                print(row[0])
                print("{:.2f}".format(row[1]))






main()