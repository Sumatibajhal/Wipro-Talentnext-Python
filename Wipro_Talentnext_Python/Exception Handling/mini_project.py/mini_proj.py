'''
You had saved the items and their price details in a text file, which you purchased yesterday from a nearby super market.
You need to know:
1. How many items did you purchase?
2. How many items are free?
3. What is the total amount you had to pay?
4. What is the discount amount?
5. What is the final amount did you pay after the discount?
Help yourself by writing a python code to do this. Include necessary code to handle the possible exceptions.
'''
def process_purchase(filename):
    try:
        with open(filename + ".txt", "r") as file:
            lines = file.readlines()

        total_amount = 0
        discount = 0
        purchased_items = 0
        free_items = 0

        for line in lines:
            line = line.strip()
            if not line:
                continue
            if line.lower().startswith("discount"):
                try:
                    discount = int(line.split()[1])
                except (IndexError, ValueError):
                    print("Invalid discount format.")
            else:
                parts = line.split()
                if len(parts) == 2:
                    item, price = parts
                    try:
                        price = int(price)
                        if price == 0:
                            free_items += 1
                        else:
                            total_amount += price
                        purchased_items += 1
                    except ValueError:
                        print(f"Invalid price for item: {item}")
                else:
                    print(f"Ignoring malformed line: {line}")

        final_amount = total_amount - discount

        print(f"Enter the file name: {filename}")
        print(f"No of items purchased: {purchased_items}")
        print(f"No of free items: {free_items}")
        print(f"Amount to pay: {total_amount}")
        print(f"Discount given: {discount}")
        print(f"Final amount paid: {final_amount}")

    except FileNotFoundError:
        print("File not found. Please check the filename and try again.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    filename = input("Enter the file name: ")
    process_purchase(filename)
