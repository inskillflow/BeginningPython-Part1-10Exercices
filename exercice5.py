# We ask the user to indicate the number of years of experience : 
numberOfYears= input ("How many years of experience do you have ?")
print(numberOfYears)

# Determining wheter the candidate is qualified for the position of the director or not  :
if int(numberOfYears) >= 8:
    print("Congratulations ! You are eligible for the director position")
else :
    print ("Sorry !")