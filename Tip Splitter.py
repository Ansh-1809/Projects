def tip_splitter():
    print("💸 Welcome to the Tip Splitter!")
    try:
        total_bill = float(input("Enter the total bill amount (₹): "))
        tip_percent = float(input("Enter tip percentage (e.g., 10 for 10%): "))
        num_people = int(input("Enter number of people to split the bill: "))

        tip_amount = total_bill * (tip_percent / 100)
        total_with_tip = total_bill + tip_amount
        amount_per_person = total_with_tip / num_people

        print(f"\nTotal Tip: ₹{tip_amount:.2f}")
        print(f"Total Amount (including tip): ₹{total_with_tip:.2f}")
        print(f"Each person should pay: ₹{amount_per_person:.2f}")
    
    except ValueError:
        print("Please enter valid numeric input.")

tip_splitter()
