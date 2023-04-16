#!/usr/bin/env python3

# Define the function factorial and what is passed in 
def factorial(n):
    # Implement a check to see if n is a non-negative integer
    while not isinstance(n, int) or n < 0:
        raise ValueError("n must be a non-negative integer")
    # To handle the specific case of n=zero the return value is set to the factorial value of 0, 1
    if n == 0:
        return 1
    # Initialising the result to 1, if this is not done, result will equal 0
    result = 1
    # Now multiply the results for every integer within n, to obtain the factorial of n
    for i in range(1, n+1):
        result *= i
    # This returns the result of the function
    return result
    
# Defining the function binomial_coefficient and what is passed into it
def binomial_coefficient(n, k):
    # This is to check that both n and k are non-negative integers, raising errors if False
    if not all(isinstance(x, int) and x >= 0 for x in (n, k)):
        raise ValueError("Both n and k must be non-negative integers")
    # Another check, to ensure that k is of greater value than n
    if k>n:
        raise ValueError("k cannot be greater than n")
    # Return the result of the binomial coefficient by passing n into the factorial function defined above
    return factorial(n)//(factorial(k) * factorial(n-k))
 
# Defining the final function pascals_triangle which calls the two prior function
def pascals_triangle(n):
# This is a check to see if n is a non-negative integer, if it is it asks for another
    if not isinstance(n, int) or n < 0:
        n = int(input("\nEnter a non-negative integer: "))
        return pascals_triangle(n)
    # Create a for loop to run_triangle_answer through the rows of the triangle
    # Start with i for all values in n
    print("\n") 
    # i refers to each row of Pascal's triangle and n in the binomial coefficient
    for i in range(n):
        # Create the empty array row to later add data into
        row = []
        # j signifies the value for k and will be used to calculate each number within the rows of i
        for j in range(i+1):
            # Now add the binomial coefficient of the values to the empty array defined  
            row.append(binomial_coefficient(i, j))
        # If the triangle is too large the rows will become hard to separate, therefore large triangles are not printed as a triangle
        if n>15:
            # Each row is printed with [] on either side, this helps separate each line when viewing
            print(row)
        # Else the triangle will be smaller and easier to interpret on a screen 
        else:
            # To have the triangle appear as a triangle, we convert it to a string
            row_str = " ".join(str(x) for x in row)
            # Centre the triangle to 6x n so that it stays far from the edge of the screen
            width = (6*n)
            row_str = row_str.center(width)
            print(row_str)

def main():
    def int_input():
        try:
            # Try to pass the integer through the function pascals_triangle
            # This function then calls binomial_coefficient, which calls the factorial function
            number = int(input("\nHow many rows of Pascal's triangle do you wish to view?\nEnter a non-negative integer: "))
            # The n number of Pascal's triangle is the number of rows -1
            n_number = number -1
            # As Pascal's triangle does not deal with negatives, an if statement is required
            if n_number == -1:
                print("\nZero lines printed, however the binomial coefficient of n 0 is 1")
            elif n_number < -1:
                print("\nPlease enter a non-negative integer")
                return int_input()
            # The function passess n which the user provides, through the pascals_triangle function
            elif isinstance(number, int) or number < 0:
                print(f"\nPascal's triangle for the binomial coefficient n {n_number}\n")
                pascals_triangle(number)
        # If a string is entered, the function will ask the user for the input again
        except ValueError:
            print("\nInvalid input. Please enter a non-negative integer.")
            return int_input()

    def should_run_program():
        # This is set up to continuously ask the user if they would like to view the triangle
        while True:
            run_triangle_answer = input("\nWould you like to view Pascal's triangle? (yes/no): ")
            if run_triangle_answer.lower() == "yes":
                try:
                    int_input()
                # In case a string or float is input, it will tell the user the error provided the wrong type of input
                except ValueError:
                    print("\nInvalid input. Please enter a non-negative integer.")
                    return int_input()
            # If the user does not wish to run the programme, then it will end and thank the user
            elif run_triangle_answer.lower() == 'no':
                print("\nThank you for using this program.\n")
                break
            # If the user does not answer the question in the way provided, it will tell the user they did not correctly input
            else:
                print("\nInvalid input, please enter 'yes' or 'no'.")
                continue
    # This is where the programme executes the function triangle_input
    should_run_program()

if __name__ == "__main__":
    main()
