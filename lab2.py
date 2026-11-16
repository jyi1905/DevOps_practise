def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    bmi= float(weight)/float(height*height)
    print("bmi =" + str(bmi))

    if bmi<18.5:
        print("underweight")
    elif 18.5<=bmi<=25.0:
        print("normalweight")
    elif bmi>=25.0:
        print("overweight")


        


calculate_bmi(weight=57, height=1.73)

