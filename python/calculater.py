print("the results in metes, in kl, z")
height = float(input("height: "))
weight = float(input("weight: "))
BMI = weight / (height * height)
if BMI < 18.5:
    print("you are underweight")
elif BMI > 25:
    print("you are overweight")
else:
    print("you are great")