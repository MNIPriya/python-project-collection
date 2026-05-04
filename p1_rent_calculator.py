#inputs we nee from user 
#total rent, food order for snacking , elctricity unitcharge per unit ,number of person
##output
# total amout we need to pay 
persons = int(input("enter the person living in room = "))
rent = int(input("enter your rent = "))
food = int(input("enter the total amout of food order = "))
electricity_spent = int(input("enter the total of electricity spent = "))
charge_per_unit = int(input("enter the charge per unit =  "))
total_bill = electricity_spent*charge_per_unit
amout = (food+rent+total_bill)//persons
print(f"each person will pay = {amout}")


