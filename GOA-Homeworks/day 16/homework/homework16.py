# Iterate over the range from 120 to 500
for number in range(120, 501):
    # Convert the number to a string to access each digit
    num_str = str(number)
    
    # Iterate over each digit in the number
    for index, digit in enumerate(num_str):
        # Check if the position is every third digit (index 2, 5, 8, ...)
        if (index + 1) % 3 == 0:
            digit = int(digit)
            
            # Print the current digit
            print(f"Digit: {digit} from number {number}")
            
            # Check if the digit is divisible by 3, 5, or 7
            if digit % 3 == 0:
                print(f"{digit} is divisible by 3")
            if digit % 5 == 0:
                print(f"{digit} is divisible by 5")
            if digit % 7 == 0:
                print(f"{digit} is divisible by 7")
                
            # Print the digit if it is even
            if digit % 2 == 0:
                print(f"{digit} is even")