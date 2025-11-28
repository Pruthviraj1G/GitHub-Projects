while True:
    print("\nHere's Your Unit Converter\n")
    H = int(input("Choose the Unit to convert\n\n1.Hour to Minutes/Seconds\n2.Kilograms to Pounds\n3.Miles to Kilometers\n4.Inches to Centimeters\n"))

    if H == 1:
        hours = float(input("Enter Hours: "))
        l = int(input("1. To Minutes\n2. To Seconds\n"))
        if l == 1:
            print("Minutes:", hours * 60)
        elif l == 2:
            print("Seconds:", hours * 3600)
        else:
            print("Invalid Input")

    elif H == 2:
        kg = float(input("Enter weight in kilograms: "))
        pounds = kg * 2.20462
        print(f"{kg} kilograms = {pounds} pounds")

    elif H == 3:
        miles = float(input("Enter distance in miles: "))
        kilometers = miles * 1.60934
        print(f"{miles} miles = {kilometers} km")

    elif H == 4:
        inches = float(input("Enter length in inches: "))
        centimeters = inches * 2.54
        print(f"{inches} inches = {centimeters} cm")

    else:
        print("Invalid Input")

    again = input("\nDo you want to convert again? (y/n): ")
    if again.lower() != "y":
        print("\nProgram ended. Goodbye!")
        break
