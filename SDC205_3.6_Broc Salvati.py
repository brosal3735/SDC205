# Import any necessary libraries (none needed for this program)

def functionOne():
    print("My Student ID is Brosal3735")

def functionTwo():
    num1 = int(input("Please enter a number: "))
    num2 = int(input("Please enter a number: "))
    sum_value = num1 + num2
    print(f"The sum of {num1} and {num2} is {sum_value}.")
    return sum_value

def functionThree(sum_param):
    if sum_param > 5:
        print("The sum is greater than 5.")
    else:
        print("The sum is 5 or less.")
    return 1234

def main():
    # Call functionOne to display the Student ID
    functionOne()
    
    # Call functionTwo to get two numbers from user, calculate sum, and store the returned value
    total = functionTwo()
    
    # Call functionThree passing the sum from functionTwo, and store the returned Student ID number
    student_id_number = functionThree(total)
    
    # Print the value returned from functionThree
    print(f"functionThree returned the value of {student_id_number}.")

main()
