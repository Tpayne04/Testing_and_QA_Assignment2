from BMI_Calculator import convertHeight, convertWeight, calculateBMI, getBMICategory


# Tests for convertWeight
def test_convertHeight_normal():
    assert convertHeight(5, 10) == 70 * 0.025

def test_convertHeight_zero_inches():
    assert convertHeight(6, 0) == 72 * 0.025

def test_convertHeight_zero_height():
    assert convertHeight(0, 0) == 0


# Tests for convertWeight
def test_convertWeight_normal():
    assert convertWeight(150) == 67.5

def test_convertWeight_zero():
    assert convertWeight(0) == 0


# Tests for calculateBMI
def test_calculate_bmi_normal():
    height = convertHeight(5, 10)
    weight = convertWeight(150)
    bmi = calculateBMI(height, weight)
    assert 18.5 <= bmi <= 24.9

def test_calculate_bmi_underweight_range():
    height = convertHeight(6, 0)
    weight = convertWeight(120)
    bmi = calculateBMI(height, weight)
    assert bmi < 18.5

def test_calculate_bmi_overweight_range():
    height = convertHeight(5, 8)
    weight = convertWeight(180)
    bmi = calculateBMI(height, weight)
    assert 25 <= bmi <= 29.9

def test_calculate_bmi_obese_range():
    height = convertHeight(5, 5)
    weight = convertWeight(220)
    bmi = calculateBMI(height, weight)
    assert bmi >= 30



def test_normal_lower_boundary():
    assert getBMICategory(18.5) == "Normal Weight"

def test_normal_upper_boundary():
    assert getBMICategory(24.9) == "Normal Weight"

def test_overweight_lower_boundary():
    assert getBMICategory(25.0) == "Overweight"

def test_obese_boundary():
    assert getBMICategory(30.0) == "Obese"