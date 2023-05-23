from functions import *

def menu():
    print("\n==== Programming Quotes ====")
    print("random : Random quote")
    print("display : Display quotes")
    print("add : Add a new quote")
    print("exit : Exit the program")

def menu():
    print("\n==== Programming Quotes ====")
    print("1. Random quote")
    print("2. All quotes")
    print("3. Add quote")
    print("4. Exit")

    print("3. Exit")


def main():
    while True:
        quotes = load_quotes("quotes.txt")
        menu()
        
        choice = input(">> ")

        if choice == "random":
            print_quote(random_quote(quotes))
        elif choice == "display":
            count = str(input("Enter the number of quotes to display: "))
            display_quotes(quotes, int(count))
            elif choice == "add":
            add_quote(quotes, "quotes.txt")
        elif choice == "exit":

        choice = input("Choose your an action (1-3): ")
        
        if choice == "1":
            print_quote(random_quote(quotes))
        elif choice == "2": # gestion de display_count()
            count = int(input("Enter the number of quotes to display: "))
            display_quotes(quotes, count)
        elif choice == "3":
            print("Add a quote")
            add_quote(quotes, "quotes.txt")
        elif choice == "4":

            print("Good bye...")
            break
        else:
            print("Invalid input")


if __name__ == "__main__":
    main()

if __name__ == "__main__":
    main()
    
if __name__ == "__main__":
    main()

