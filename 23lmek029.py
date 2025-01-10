'''

import matplotlib.pyplot as plt


class Investment:
    def __init__(self, initial_balance, interest_rate, monthly_add, yearly_withdraw):
        self.balance = initial_balance
        self.interest_rate = interest_rate
        self.monthly_add = monthly_add
        self.yearly_withdraw = yearly_withdraw
        self.yearly_balances = []  # To track yearly balances for graph

    def calculate_balance(self, years):
        for year in range(1, years + 1):
            for month in range(1, 13):
                # Apply monthly interest
                self.balance += self.balance * (self.interest_rate / 12)
                # Add monthly deposit
                self.balance += self.monthly_add

            # Apply yearly withdrawal
            self.balance -= self.yearly_withdraw

            # Track yearly balance for plotting
            self.yearly_balances.append(self.balance)

    def show_text(self):
        print("\nYearly Investment Balances:")
        for year, balance in enumerate(self.yearly_balances, start=1):
            print(f"Year {year}: {balance:.2f} TRY")

    def show_graph(self):
        years = range(1, len(self.yearly_balances) + 1)
        plt.plot(years, self.yearly_balances, marker='o', color='b', label="Balance Over Time")
        plt.xlabel("Years")
        plt.ylabel("Balance (TRY)")
        plt.title("Investment Growth Over Time")
        plt.legend()
        plt.grid(True)
        plt.show()

def main():
    investment = None  # Define globally to retain state between choices

    while True:
        print("\nInvestment Management System")
        print("1. Calculate investment")
        print("2. Show investment as text")
        print("3. Show investment graph")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            # Get input values from the user
            initial_balance = float(input("Enter initial balance (TRY): "))
            interest_rate = float(input("Enter annual interest rate (%): ")) / 100
            monthly_add = float(input("Enter monthly addition amount (TRY): "))
            yearly_withdraw = float(input("Enter annual withdrawal amount (TRY): "))

            # Create investment object
            investment = Investment(initial_balance, interest_rate, monthly_add, yearly_withdraw)

            # Calculate investment for 10 years
            investment.calculate_balance(10)
            print("Investment calculated successfully!")

        elif choice == "2":
            if investment:
                investment.show_text()
            else:
                print("Please calculate the investment first.")

        elif choice == "3":
            if investment:
                investment.show_graph()
            else:
                print("Please calculate the investment first.")

        elif choice == "4":
            print("Exiting...")
            break  # Exit the program

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()








import matplotlib.pyplot as plt
import time


def bubble_sort_visualize(array):
    n = len(array)
    for i in range(n):
        for j in range(n - i - 1):
            # Display the current comparison
            print(f"Comparing {array[j]} with {array[j + 1]}")
            if array[j] > array[j + 1]:
                # Swap if the left element is greater
                array[j], array[j + 1] = array[j + 1], array[j]

            # Visualize the current state of the array
            plt.bar(range(len(array)), array, color='skyblue')
            plt.xlabel("Index")
            plt.ylabel("Value")
            plt.title("Bubble Sort Progress")
            plt.pause(0.5)  # Pause for animation effect
            plt.clf()  # Clear the plot for the next step

        print(f"Array after pass {i + 1}: {array}")

    # Show the final sorted array
    plt.bar(range(len(array)), array, color='green')
    plt.xlabel("Index")
    plt.ylabel("Value")
    plt.title("Sorted Array")
    plt.show()


def main():
    while True:
        print("\nBubble Sort Visualization")
        print("1. Sort an array")
        print("2. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            # Input the array to sort
            raw_input = input("Enter the array elements separated by spaces: ")
            array = list(map(int, raw_input.split()))
            bubble_sort_visualize(array)
            print("Sorting complete!")
        elif choice == "2":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()








import matplotlib.pyplot as plt

def calculate_snow_possibility(temperature, humidity):
    snow_possibility = []
    for temp, hum in zip(temperature, humidity):
        if temp < 0:
            possibility = hum // 2  # Higher humidity increases snow chance
        else:
            possibility = 0
        snow_possibility.append(possibility)
    return snow_possibility

def plot_forecast(temp, hum, snow_possibility):
    years = range(len(temp))
    plt.figure(figsize=(10, 6))

    # Bar plot for temperature and humidity
    plt.bar(years, temp, color='blue', label='Temperature (°C)', alpha=0.6)
    plt.bar(years, hum, color='orange', label='Humidity (%)', alpha=0.6)

    # Line plot for snow possibility
    plt.plot(years, snow_possibility, color='green', marker='o', label='Snow Possibility (%)')

    plt.xlabel("Days")
    plt.ylabel("Values")
    plt.title("Weather Forecast: Snow Possibility")
    plt.legend()
    plt.grid(True)
    plt.show()

def main():
    while True:
        print("\nWeather Forecast System")
        print("1. Calculate snow possibility")
        print("2. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            # Input temperature and humidity data
            temp = list(map(int, input("Enter temperature data (space-separated): ").split()))
            hum = list(map(int, input("Enter humidity data (space-separated): ").split()))

            if len(temp) != len(hum):
                print("Error: Temperature and humidity data must have the same length!")
                continue

            # Calculate snow possibility
            snow_possibility = calculate_snow_possibility(temp, hum)
            print("Calculated Snow Possibility:", snow_possibility)

            # Plot the data
            plot_forecast(temp, hum, snow_possibility)
        elif choice == "2":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()









import matplotlib.pyplot as plt

class BudgetTracker:
    def __init__(self):
        self.expenses = []  # Stores expense records as tuples (category, amount, description)
        self.incomes = []  # Stores income records as tuples (source, amount)
        self.balance = 0  # Tracks the current balance

    def add_expense(self, category, amount, description):
        self.expenses.append((category, amount, description))
        self.balance -= amount

    def add_income(self, source, amount):
        self.incomes.append((source, amount))
        self.balance += amount

    def display_records(self):
        print("\nIncome Records:")
        for source, amount in self.incomes:
            print(f"- {source}: {amount:.2f} TRY")

        print("\nExpense Records:")
        for category, amount, description in self.expenses:
            print(f"- {description} ({category}): {amount:.2f} TRY")

    def display_balance(self):
        print(f"\nCurrent Balance: {self.balance:.2f} TRY")
        if self.balance < 0:
            print("Warning: Your balance is negative!")

    def display_pie_chart(self):
        if not self.expenses:
            print("No expenses to display in the pie chart.")
            return

        categories = {}
        for category, amount, _ in self.expenses:
            categories[category] = categories.get(category, 0) + amount

        labels = list(categories.keys())
        sizes = list(categories.values())

        plt.figure(figsize=(8, 8))
        plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired.colors)
        plt.title("Monthly Expenses Breakdown")
        plt.show()


def main():
    tracker = BudgetTracker()

    while True:
        print("\nBudget Management System")
        print("1. Add an expense")
        print("2. Add an income")
        print("3. Display records")
        print("4. Display balance")
        print("5. Display pie chart of expenses")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            category = input("Enter expense category (e.g., market, car, subscriptions): ")
            amount = float(input("Enter expense amount (TRY): "))
            description = input("Enter a description for the expense: ")
            tracker.add_expense(category, amount, description)
            print("Expense added successfully!")

        elif choice == "2":
            source = input("Enter income source (e.g., salary, promotion): ")
            amount = float(input("Enter income amount (TRY): "))
            tracker.add_income(source, amount)
            print("Income added successfully!")

        elif choice == "3":
            tracker.display_records()

        elif choice == "4":
            tracker.display_balance()

        elif choice == "5":
            tracker.display_pie_chart()

        elif choice == "6":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()







import matplotlib.pyplot as plt

class ShoppingCart:
    def __init__(self, balance):
        self.balance = balance
        self.list_items = []  # Available items (name, quantity, price)
        self.cart_items = []  # Cart items (name, quantity, price)
        self.total_cart_price = 0

    def add_to_list(self, name, quantity, price):
        """Add items to the available list."""
        self.list_items.append((name, quantity, price))

    def add_to_cart(self, name, quantity):
        """Add items to the cart and subtract from available list."""
        for item in self.list_items:
            if item[0] == name:
                _, available_quantity, price = item

                if quantity > available_quantity:
                    print(f"Error: Not enough {name} in the list.")
                    return

                total_price = price * quantity

                if self.balance < total_price:
                    print(f"Error: Not enough balance to add {name} to the cart.")
                    return

                # Update the list and cart
                self.list_items.remove(item)
                if available_quantity > quantity:
                    self.list_items.append((name, available_quantity - quantity, price))
                self.cart_items.append((name, quantity, price))

                self.balance -= total_price
                self.total_cart_price += total_price
                print(f"{name} added to the cart successfully!")
                return

        print(f"Error: {name} is not available in the list.")

    def compare_prices(self):
        """Compare prices between the list and cart."""
        print("\nPrice Comparison:")
        all_items = {item[0]: item for item in self.list_items + self.cart_items}
        for name, (name, quantity, price) in all_items.items():
            if name in [cart_item[0] for cart_item in self.cart_items]:
                cart_price = [cart_item[2] for cart_item in self.cart_items if cart_item[0] == name][0]
                diff = ((cart_price - price) / price) * 100
                status = "expensive" if diff > 0 else "cheaper"
                print(f"{name} is {abs(diff):.2f}% {status} in the cart.")
            else:
                print(f"{name} is only in the list and not in the cart.")

    def display_cart_summary(self):
        """Display the total balances for the list and cart."""
        total_list_balance = sum(item[2] * item[1] for item in self.list_items)
        print(f"\nTotal list balance: {total_list_balance:.2f} TRY with {len(self.list_items)} items.")
        print(f"Total cart balance: {self.total_cart_price:.2f} TRY with {len(self.cart_items)} items.")

    def show_bar_graph(self):
        """Display a bar graph of the items and their prices in the cart."""
        if not self.cart_items:
            print("No items in the cart to display graph.")
            return

        items = [item[0] for item in self.cart_items]
        prices = [item[2] for item in self.cart_items]

        plt.figure(figsize=(10, 6))
        plt.bar(items, prices, color='skyblue')
        plt.xlabel("Items")
        plt.ylabel("Prices (TRY)")
        plt.title("Prices of Items in the Cart")
        plt.grid(axis='y')
        plt.show()


def main():
    balance = float(input("Enter your initial balance (TRY): "))
    shopping_cart = ShoppingCart(balance)

    print("\nShopping Cart System")
    print("1. Add item to list")
    print("2. Add item to cart")
    print("3. Compare prices")
    print("4. Display cart summary")
    print("5. Show bar graph")
    print("6. Exit")

    while True:
        choice = input("\nEnter your choice: ")

        if choice == "1":
            name = input("Enter item name: ")
            quantity = int(input("Enter item quantity: "))
            price = float(input("Enter item price (TRY): "))
            shopping_cart.add_to_list(name, quantity, price)
            print("Item added to list successfully!")

        elif choice == "2":
            name = input("Enter item name: ")
            quantity = int(input("Enter item quantity: "))
            shopping_cart.add_to_cart(name, quantity)

        elif choice == "3":
            shopping_cart.compare_prices()

        elif choice == "4":
            shopping_cart.display_cart_summary()

        elif choice == "5":
            shopping_cart.show_bar_graph()

        elif choice == "6":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
'''
