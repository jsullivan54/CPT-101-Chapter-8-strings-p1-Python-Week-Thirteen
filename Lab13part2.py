# Name: Johnathan Sullivan
# Date: 11/22/2024
# Lab Number & Part: Lab13_part2


# Program Description:
# This program reads individual strings from the user's input for Full_Name, Address_Line, City, State and ZipCode - /
# The program then stores these in separate variables. Prior to printing an Address Label, convert the data using the various string/
# methods shown in Chapter 8: More About Strings. Additional Requirements:

# Capitalize only the First letter of the first and last name. You can use upper, lower, and split functions where appropriate.
# Remove any punctuation or special characters used in the address line and CAPITALIZE entire Address_Line, including CITY/STATE.
# Check if an entered Zip Code is 5 digits. If it isn't, ask user to RE-ENTER Zip Code until a VALID zip code is entered. /
# Hint: You will need a while loop!


# Define the Main Function

def main():
    full_name = input("Please Enter Your Full Name: ").strip()    # Take the users full name as input

    address = input("Please Enter Your Address: ").strip()     # Take the users address as input

    city = input("Please Enter Your City Name: ").strip()      # Take the users city as input

    state = ""      # Take the users state as input
    while len(state) != 2 or not state.isalpha():   # Make sure the state is not more than two characters, and is not digit
        if state:
            print("That's Not a Correct State Name! ") # If the state input is incorrect reject it and ask for correct input
        state = input("Please Enter Your Two Digit State Name (e.g. New York = NY): ").strip().upper() # Get the correct input

    zipcode = "" # start the zip code input

    while len(zipcode) != 5 or not zipcode.isdigit(): # Make sure the input is 5 digits

        if zipcode:
            print("That is Not a Correct 5-digit Zip Code! ") # Else print error

        zipcode = input("Please Enter Your Zip Code (e.g. 14580): ").strip() # Accept the correct zipcode input

# Start the full formatted label
    formatted_label = ""

# Take the Full name and make sure the first letter of the first and last name are upper and the following letter lowercase
    for word in full_name.split():
        formatted_label += word[0].upper() + word[1:].lower() + " "

# Turn the address into a correctly formatted all caps
    for char in address:
        if char.isalnum() or char.isspace():

            formatted_label += char.upper()

# Make the city input all caps
    formatted_label += "\n" + city.upper()

    formatted_label += ", " + state + ", " + zipcode

# Print a simple header to separate the label from the input
    print("\n==== Address Label (Soon to be the base of my citation generator Thank you) ====")
    print(formatted_label.strip())


# Close the program
if __name__ == '__main__':
    main()

