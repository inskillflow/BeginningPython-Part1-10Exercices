### Definition of the `show_person` Function
def show_person(name, age=18):  # Function definition with a default parameter for age
    # Displays the person's name and age
    print(f"Name: {name}, Age: {age}")

#### Examples of Function Calls
show_person("Maria", 26)  # Calling the function with specified name and age
show_person("Peter")      # Calling the function with only the name, default age is used


#### Expected Result:
# Name: Maria, Age: 26
# Name: Peter, Age: 18


#### Explanations:
#- The `show_person()` function is defined with two parameters: `name` and `age`. The `age` parameter has a default value of 18. This means that if no age is provided when the function is called, 18 will be used as the age.
#- When the function is called with both arguments (as in `show_person("Maria", 26)`), it uses the provided age value.
#- When it is called with only one argument (as in `show_person("Peter")`), it uses the default value for age, which is 18.
#- The function then prints the person's name and age using a formatted string.