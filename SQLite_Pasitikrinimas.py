import sqlite3

data = sqlite3.connect("finance.sqlite")
cursor = data.cursor()


def income(type, amount, category):
    cursor.execute("INSERT INTO finances (type, amount, category) VALUES (?, ?, ?)",
                   (type, amount, category))
    data.commit()
    print("Information was successfully added.")


def expenses(type, amount, category):
    cursor.execute("INSERT INTO finances (type, amount, category) VALUES (?, ?, ?)",
                   (type, amount, category))
    data.commit()
    print("Information was successfully added.")


def enter_income():
    type = "income"
    amount = int(input("Enter the amount of income: "))
    category = input("Enter the category from where the income was received: ")
    income(type, amount, category)


def enter_expenses():
    type = "expenses"
    amount = int(input("Enter the amount of income: "))
    category = input("Enter the category from where the income was received: ")
    income(type, amount, category)


def get_balance():
    cursor.execute("SELECT SUM(amount) FROM finances WHERE type='income'")
    cursor.execute("SELECT SUM(amount) FROM finances WHERE type='expense'")

    total_income = cursor.fetchone()[0] or 0
    total_expenses = cursor.fetchone()[0] or 0

    balance = total_income - total_expenses
    print(f"The balance of your finances is: {balance}")


def get_all_incomes():
    cursor.execute("SELECT * FROM finances WHERE type='income'")
    incomes = cursor.fetchall()
    print("The list of incomes that are in the table:")
    for income in incomes:
        print(income)


def get_all_expenses():
    cursor.execute("SELECT * FROM finances WHERE type='expenses'")
    expenses = cursor.fetchall()
    print("The list of expenses that are in the table:")
    for expense in expenses:
        print(expense)


def delete_data():
    data_id = int(input("Please enter the ID number for income or expense you want to delete: "))
    cursor.execute("DELETE FROM finances WHERE id=?", (data_id,))
    data.commit()


def update_data():
    data_id = int(input("Please enter the ID number for income or expense you want to update: "))
    new_type = input("What is the new type (income or expense)?: ")
    new_amount = float(input("What is the new amount?: "))
    new_category = input("What is the new category?: ")
    cursor.execute("UPDATE finances SET type=?, amount=?, category=? WHERE id=?",
                   (new_type, new_amount, new_category, data_id))
    data.commit()


def finance_joke():
    print("Why did the savings account take up meditation?\nIt wanted to find its “inner balance”!")


def main_menu():
    while True:
        print("--- Finance menu ---")
        print("--> Enter '1' to add income.")
        print("--> Enter '2' to add expenses.")
        print("--> Enter '3' to get balance.")
        print("--> Enter '4' to get all income.")
        print("--> Enter '5' to get all expenses.")
        print("--> Enter '6' to delete income or expense.")
        print("--> Enter '7' to update income or expense.")
        print("--> Want to hear a joke about finance? Enter --> 'y' for yes and 'n' for no. ")
        print("--> Enter 'exit' to exit the program.")
        choice = input("Choose an option by entering the number: ")

        if choice == "1":
            enter_income()
        elif choice == "2":
            get_balance()
        elif choice == "3":
            get_all_incomes()
        elif choice == "4":
            get_all_incomes()
        elif choice == "5":
            get_all_expenses()
        elif choice == "6":
            delete_data()
        elif choice == "7":
            update_data()
        elif choice == 'y':
            finance_joke()
        elif choice == 'n':
            no = input("Are you sure you don't want to hear a joke? ('y' or 'n'): ")
            if no == 'n':
                print("Fine, go choose another option then.")
            if no == 'y':
                print("Great! Here you go:\nWhy did the savings account take up meditation?"
                      "\nIt wanted to find its “inner balance”!")
        elif choice == "exit":
            print("Thank you for using the program. Goodbye!")
            break
        else:
            print("Invalid. Please choose from the menu with options.")


if __name__ == "__main__":
    main_menu()

data.close()
