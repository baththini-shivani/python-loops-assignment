# Name: [Your Name]
# Roll Number: [Your Roll Number]
# Assignment: Python Loops & Automation - Subjective Question

print("===== Task 1: Find Maximum and Minimum =====")

temperatures = [28, 32, 35, 29, 31, 27, 30]

highest = temperatures[0]
lowest = temperatures[0]

for temp in temperatures:
    if temp > highest:
        highest = temp
    if temp < lowest:
        lowest = temp
print("Highest Temperature:", highest)
print("Lowest Temperature:", lowest)


print("\n===== Task 2: Count Hot Days =====")
temperatures = [28, 32, 35, 29, 31, 27, 30]

highest = temperatures[0]
lowest = temperatures[0]

count_above_30 = 0

for temp in temperatures:
    if temp > highest:
        highest = temp
    if temp < lowest:
        lowest = temp
    if temp <= 30:
        continue
    
    count_above_30 += 1

print("Hot Days (>30°C):", count_above_30)


print("\n===== Task 3: Alert System =====")
temperatures = [28, 32, 35, 40, 31, 33, 30]

count_hot_days = 0

for day in range(len(temperatures)):
    temp = temperatures[day]

    if temp >= 40:
        print("Hot Days before alert:", count_hot_days)
        print(f"Alert! Extreme temperature {temp}°C detected on Day {day + 1}")
        break

    if temp <= 30:
        continue
      
    count_hot_days += 1
