#Mohmika Kapoor - 21BCT0027
import random
import time
from app import record_sensor_data

# Simulate sensor data for ECG, temperature, and SPO2
def generate_sensor_data():
    while True:
        # Simulate random values for the sensors
        ecg = random.randint(600, 1000)  # Example range for ECG (in milliVolts)
        temperature = round(random.uniform(36.0, 39.0), 2)  # Temperature in Celsius, rounded to 2 decimal places
        spo2 = random.randint(90, 100)  # SPO2 in percentage
        
        # Print the generated data
        print(f"Generated ECG: {ecg}, Temperature: {temperature}, SPO2: {spo2}")
        
        # Scale the temperature to an integer by multiplying by 100 to avoid decimal issues
        scaled_temperature = int(temperature * 100)
        
        # Record the generated data to the blockchain
        record_sensor_data(ecg, scaled_temperature, spo2)
        
        # Wait for 5 seconds before generating the next set of values
        time.sleep(5)

if __name__ == '__main__':
    generate_sensor_data()
