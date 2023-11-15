def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def meters_to_feet(meters):
    return meters * 3.28084

def feet_to_meters(feet):
    return feet / 3.28084

def kilograms_to_pounds(kilograms):
    return kilograms * 2.20462

def pounds_to_kilograms(pounds):
    return pounds / 2.20462

def unit_converter():
    print("Welcome to the Unit Converter!")
    while True:
        print("\nSelect an option:")
        print("1. Temperature Converter (Celsius to Fahrenheit / Fahrenheit to Celsius)")
        print("2. Length Converter (Meters to Feet / Feet to Meters)")
        print("3. Weight Converter (Kilograms to Pounds / Pounds to Kilograms)")
        print("4. Quit")

        choice = input("Enter the number of your choice: ")

        if choice == '1':
            value = input("Enter the temperature value: ")
            try:
                value = float(value)
                source_unit = input("Enter source unit (C for Celsius / F for Fahrenheit): ").upper()
                if source_unit == 'C':
                    result = celsius_to_fahrenheit(value)
                    target_unit = 'Fahrenheit'
                elif source_unit == 'F':
                    result = fahrenheit_to_celsius(value)
                    target_unit = 'Celsius'
                else:
                    print("Unsupported unit. Please enter C or F.")
                    continue
                print(f"{value} {source_unit} is {result} {target_unit}")
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
        
        elif choice == '2':
            value = input("Enter the length value: ")
            try:
                value = float(value)
                source_unit = input("Enter source unit (M for Meters / F for Feet): ").upper()
                if source_unit == 'M':
                    result = meters_to_feet(value)
                    target_unit = 'Feet'
                elif source_unit == 'F':
                    result = feet_to_meters(value)
                    target_unit = 'Meters'
                else:
                    print("Unsupported unit. Please enter M or F.")
                    continue
                print(f"{value} {source_unit} is {result} {target_unit}")
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
        
        elif choice == '3':
            value = input("Enter the weight value: ")
            try:
                value = float(value)
                source_unit = input("Enter source unit (K for Kilograms / P for Pounds): ").upper()
                if source_unit == 'K':
                    result = kilograms_to_pounds(value)
                    target_unit = 'Pounds'
                elif source_unit == 'P':
                    result = pounds_to_kilograms(value)
                    target_unit = 'Kilograms'
                else:
                    print("Unsupported unit. Please enter K or P.")
                    continue
                print(f"{value} {source_unit} is {result} {target_unit}")
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
        
        elif choice == '4':
            print("Thank you for using the Unit Converter. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option (1, 2, 3, or 4).")

if __name__ == "__main__":
    unit_converter()


