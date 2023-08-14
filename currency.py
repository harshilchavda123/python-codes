#open the currencyData file as f
with open('currencyData.txt') as f:
	lines = f.readlines()
#read lines

#creat dictionary as currencyDict for currencyData file
currencyDict = {}
for line in lines:
#make data parsed and split the lines
	parsed = line.split("\t")
	currencyDict[parsed[0]] = parsed[1]
#enter amount in integer

#enter amount in integer
amount = int(input("Enter amount:\n"))
#this is currency name in option

#print name of currency in currencyData file
print("Enter the name of the currency you want to convert this amount to? Available Options:\n")
#enter currency name in option you want to convert this amount
[print(item) for item in currencyDict.keys()]
#enter currency name in option you want to convert this amount
currency = input("Please enter one of these values: \n")
#final result print for you
print(f"{amount} INR is equal to {amount *float(currencyDict[currency])} {currency}")

#This is a pdf, when you try the code, it will convert to exe file
#currencyData file link is in file:///C:/Users/DELL/Downloads/currencyData.pdf