# Basic Calorimeter Program
# For 1st Year 1st Semester B.Tech Students

# Principle: Heat lost = Heat gained
# Formula:
# (m1 * c1 * (T1 - Tf)) = (m2 * c2 * (Tf - T2))

print("=== Basic Calorimeter Calculation ===")

# Taking input values
m1 = float(input("Enter mass of hot substance (kg): "))
c1 = float(input("Enter specific heat of hot substance (J/kg°C): "))
T1 = float(input("Enter initial temperature of hot substance (°C): "))

m2 = float(input("Enter mass of cold substance (kg): "))
c2 = float(input("Enter specific heat of cold substance (J/kg°C): "))
T2 = float(input("Enter initial temperature of cold substance (°C): "))

# Calculate final temperature (Tf)
Tf = (m1 * c1 * T1 + m2 * c2 * T2) / (m1 * c1 + m2 * c2)

# Calculate heat lost by hot body and gained by cold body
Q_hot = m1 * c1 * (T1 - Tf)
Q_cold = m2 * c2 * (Tf - T2)

# Display results
print("\n=== RESULTS ===")
print("Final Temperature of mixture = ", round(Tf, 2), "°C")
print("Heat lost by hot substance = ", round(Q_hot, 2), "J")
print("Heat gained by cold substance = ", round(Q_cold, 2), "J")

print("\n(According to principle of calorimetry, heat lost = heat gained)")