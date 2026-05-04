name = input("enter your name")
age = input("enter your age")
SubA  = int(input ("enter your marks in subject A"))
SubB = int(input ("enter your marks in subject B"))
SubC  = int(input ("enter your marks in subject C "))
totalMarks = SubA + SubB + SubC
totalPercent = totalMarks / 3 
print(f"name : {name}")
print(f"age :{age}")
print(f"{name} secured total marks of {totalMarks} for 300 and percentage of {totalPercent}")
if totalPercent >= 36 :
    print(f"you are pass with {totalPercent}%")
else:
    print(f"you are fail , good luck next time ")