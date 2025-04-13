import numpy as np

kg = input("체중(kg): ")
cm = input("키(cm): ")

BMI = float(kg)/((float(cm)/100)**2)
print(f"BMI: {BMI:.01f}")