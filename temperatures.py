def main():
    temperatures = 0

    choice = input("Which one you want to covert to?(C\F):").upper()
    if choice == "C":
        temperatures = convert_to_celsius()
    if choice == "F":
        temperatures = convert_to_fahrenheit()

    print(f"The converted temperatures are: {temperatures}")


def convert_to_fahrenheit():
    celsius = float(input("Enter the celsius: "))
    fahrenheit = 9 / 5 * celsius + 32
    temperatures = f"{fahrenheit:.2f}°F"
    return temperatures


def convert_to_celsius():
    fahrenheit = float(input("Enter the fahrenheit: "))
    celsius = 5 / 9 * (fahrenheit - 32)
    temperatures = f"{celsius:.2f}°C"
    return temperatures


main()
