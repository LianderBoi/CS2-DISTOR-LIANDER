# Travel Fare Calculator
import math

FARE_RATE = 14

while True:
	name = input("Enter passenger name: ").strip()
	if name:
		break
	print("Passenger name cannot be empty.")

while True:
	try:
		distance = float(input("Enter distance (km): "))
		if math.isfinite(distance) and distance > 0:
			break
		print("Distance must be a number greater than 0.")
	except ValueError:
		print("Please enter a valid number for the distance.")

while True:
	try:
		passengers = int(input("Enter number of passengers: "))
		if passengers > 0:
			break
		print("Number of passengers must be a positive whole number.")
	except ValueError:
		print("Please enter a positive whole number of passengers.")

total_fare = distance * FARE_RATE * passengers

print("\nPassenger:", name)
print("Total Fare: PHP", round(total_fare, 2))