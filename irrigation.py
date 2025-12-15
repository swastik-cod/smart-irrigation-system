soil_moisture = int(input("Enter soil moisture level (0-100): "))
temperature = int(input("Enter temperature (°C): "))

if soil_moisture < 40:
    print("Soil is dry")
    print("Irrigation pump ON")
else:
    print("Soil has sufficient moisture")
    print("Irrigation pump OFF")
