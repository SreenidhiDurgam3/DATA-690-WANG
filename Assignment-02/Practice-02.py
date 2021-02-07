#setting an empty list list1 to store values
list1 = [] 
#Using for loop for 10 integer inputs
for i in range(1, 11):
    num = int(input('Enter an Integer:'))
    #Printing the user provided input values
    print(f"Integer #{i}:",num)
    #appending the provided input values in the list1
    list1.append(num)

#Printing the list of values
print("The entered values in a list are:",list1)

#Printing the minimum and maximum of list using min and max 
print("Minimum value of the list is:",min(list1))
print("Maximum value of the list is:",max(list1))
#storing range1 as range of the list of provided values
range1 = (min(list1),max(list1))
print("Range of the list is:",range1)

#Printing mean as sum of values / length of list
print("Mean of the list is:",sum(list1)/len(list1))

#calculating variance with 2 different formulas - sample variance is divided by (len(list1)-1) and population variance by (len(list1))

varRes = sum([(xi - (sum(list1)/len(list1)))**2 for xi in list1]) / (len(list1) -1)

varRes1 = sum([(xi - (sum(list1)/len(list1)))**2 for xi in list1]) / (len(list1))

print("Sample Varience of the list is:",varRes)
print("Population Varience of the list is:",varRes1)

#Standard deviation is square root of variance

print("Standard deviation of the list is:",(varRes)**(1/2))
