# Name: Johnathan Sullivan
# Date: 11/24/2024
# Lab Number & Part: Lab13_part3

# This program uses a function that accepts a string as an argument /
# and returns the number of vowels and consonants.

# It then prints both vowels and consonants

# It utilizes a return statement to return both vowels and consonants to the main function


# Define the Main function

def main():

    user_string_input = input("Please Enter a String: ")    # Take end user string input

    vowels = "aeiouAEIOU"    # Label vowels

    vowel_count = 0    # Start a Vowel Count

    consonant_count = 0    # Start a Consonant count

    for char in user_string_input:    # Start a loop for determining the vowels and consonants

        if char.isalpha():    # Make sure that the char. are letters

            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1 # Determine consonants

    print(f"Number of Vowels: {vowel_count}")    # Print the number of Vowels
    print(f"Number of consonants: {consonant_count}")    # Print the number of Consonants


    return vowel_count, consonant_count    # The return function


# End and Close the program
if __name__ == '__main__':

    main()






