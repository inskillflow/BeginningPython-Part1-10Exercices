### 7.1. Final Result of the Given Code
# Program to print an asterisk '*' multiple times using a while loop
i = 0
while True:  # Infinite loop
    print('*')  # Prints an asterisk
    i = i + 1  # Increments the counter i
    if i >= 21:  # Checks if i is greater than or equal to 21
        break  # Exits the loop if i is greater than or equal to 21
#This code will print the asterisk '*' 21 times.


### 7.2. Modifying the Break Statement with Continue
# Modified program to replace 'break' with 'continue'

i = 0
while True:  # Infinite loop
    print('*')  # Prints an asterisk
    i = i + 1  # Increments the counter i
    if i >= 21:  # Checks if i is greater than or equal to 21
        continue  # Continues the loop if i is greater than or equal to 21


#With the 'continue' statement, this code will create an infinite loop that prints the asterisk '*' indefinitely.
#### Explanation:
#- In the first program (7.1), the while loop stops after printing the asterisk 21 times, thanks to the break statement.
#- In the second program (7.2), by replacing break with continue, the loop never stops. It continues indefinitely because the while True condition is always true, and continue simply returns to the beginning of the loop without changing this condition. Therefore, the result is not the same as in the first program.
