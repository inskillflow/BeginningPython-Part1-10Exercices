line1= "2024-03-29,38"
print(line1)
(var1,var2)= line1.split(',',1)
print(var1)
print(var2)
print ('%s\t%s' % (var1,var2))

# line1= "2024-03-29,38" string will be splitted into 2 parts 
# part 1 is the date (before the , delimiter) 2024-03-29
# part 2 is the age (after the , delimiter) 
# In this function  split(',',1) : 
# The delimiter is the parameter ',' 
# The sencond parameter (1) indicates that we will perform only one split
# final result will be as follows : 2024-03-29      38 (separated by a tabulation)
# You can try this code as well :
# print("At this date %s , I will have %s old" % (var1, var2))

