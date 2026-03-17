def convertHeight(feet, inches):
    totalInches = (feet*12) + inches
    heightM = totalInches * 0.025

    return heightM

def convertWeight(weight):
    weightKG = weight * 0.45

    return weightKG

def calculateBMI(height, weight):
    bmi = weight / (height**2)

    return bmi

def getBMICategory(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi <= 24.9:
        return "Normal Weight"
    elif 25 <= bmi <= 29.9:
        return "Overweight"
    else:
        return "Obese"

if __name__ == "__main__":
    print("Please enter your height.")
    feet = int(input("Feet: "))
    inches = int(input("Inches: "))
    print()

    print("Please enter your weight in pounds.")
    pounds = int(input("Weight: "))
    print()

    meters = convertHeight(feet, inches)
    kilograms = convertWeight(pounds)

    bmi = calculateBMI(meters, kilograms)

    print(f"Your BMI: {bmi} \n")

    print(getBMICategory(bmi))

    