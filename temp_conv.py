def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def get_temperature():
    while True:
        temp = float(input("Enter temperature value: "))
        return temp

def results():
    print(" Temperature Converter ")
    print("1: Celsius to Fahrenheit")
    print("2: Fahrenheit to Celsius")

    choice = input("Choose an option (1 or 2): ")

    if choice == "1":
        celsius = get_temperature()
        print(f"{celsius}°C is {celsius_to_fahrenheit(celsius):.2f}°F")
    elif choice == "2":
        fahrenheit = get_temperature()
        print(f"{fahrenheit}°F is {fahrenheit_to_celsius(fahrenheit):.2f}°C")
    else:
        print("Invalid choice! Please enter 1 or 2.")

results()