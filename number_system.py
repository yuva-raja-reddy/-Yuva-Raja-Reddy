def hex_to_oct(hexadecimal):
    decimal = int(hexadecimal, 16)  # Convert hex to decimal
    return oct(decimal)  # Convert decimal to octal

def oct_to_hex(octal):
    decimal = int(octal, 8)  # Convert octal to decimal
    return hex(decimal)  # Convert decimal to hex

if __name__ == "__main__":
    choice = input("Choose conversion type (1 for Hex to Oct, 2 for Oct to Hex): ")

    if choice == "1":
        hexadecimal = input("Enter a hexadecimal number: ")
        print("Octal equivalent:", hex_to_oct(hexadecimal))
    elif choice == "2":
        octal = input("Enter an octal number: ")
        print("Hexadecimal equivalent:", oct_to_hex(octal))
    else:
        print("Invalid choice. Please select 1 or 2.")