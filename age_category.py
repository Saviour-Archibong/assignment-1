age = int(input("enter yuor age: "))
if age < 13:
    print("you are a child")
elif age >= 13 and age < 18:
    print("you are a teneger")    
elif age >= 18 and age < 60:
    print("you are an adult")
else:
    print("you are a senior citizen")       