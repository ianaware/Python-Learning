# Initialize variables
maximum = None
minimum = None

while True:  # Start an infinite loop
    num_str = input("Enter a number: ")  # Prompt the user for input

    if num_str == "done":  # Check if the user wants to end the loop
        break  # Exit the loop

    try:
        num = int(num_str)  # Try converting the input to an integer

        # Update largest and smallest numbers
        if maximum is None or num > maximum:
            maximum = num
        if minimum is None or num < minimum:
            minimum = num

    except ValueError:  # Catch the exception if conversion fails
        print("Invalid input")  # Print an error message, corrected for case and wording

# Print the results outside the loop, using the specified wording
print("Maximum is", maximum)
print("Minimum is", minimum)
