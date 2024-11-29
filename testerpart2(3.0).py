def main():
    full_name_input = input("Enter Full Name: ").strip()
    address_input = input("Enter Address Line: ").strip()
    city_input = input("Enter City: ").strip()
    state_input = input("Enter State (2 letters): ").strip().upper()

    zip_code_input = ""
    while len(zip_code_input) != 5 or not zip_code_input.isdigit():
        if zip_code_input:
            print("Invalid Zip Code. Please enter a 5-digit Zip Code.")
        zip_code_input = input("Enter Zip Code (5 digits): ").strip()

    # Using only one variable to format and transform everything
    formatted_label = ""

    # Capitalize full name
    for word in full_name_input.split():
        formatted_label += word[0].upper() + word[1:].lower() + " "

    # Remove punctuation from address line and convert to uppercase
    for char in address_input:
        if char.isalnum() or char.isspace():
            formatted_label += char.upper()

    # Convert city to uppercase
    formatted_label += "\n" + city_input.upper()

    # Add state and zip code
    formatted_label += ", " + state_input + ", " + zip_code_input

    # Print the formatted address label
    print("\n=== Address Label ===")
    print(formatted_label.strip())  # Remove trailing space

main()

