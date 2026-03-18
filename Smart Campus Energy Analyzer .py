n = int(input("Enter number of buildings: "))

energy = [0] * n

for i in range(n):
    energy[i] = int(input("Enter energy reading: "))


data = {
    "efficient": [],
    "moderate": [],
    "high": [],
    "invalid": []
}

reg = "AP24110011729"
last_digit = int(reg[-1])

if last_digit % 2 != 0:
    high_limit = 170
else:
    high_limit = 150


for i in range(n):

    if energy[i] < 0:
        data["invalid"].append(energy[i])

    elif energy[i] <= 50:
        data["efficient"].append(energy[i])

    elif energy[i] <= high_limit:
        data["moderate"].append(energy[i])

    else:
        data["high"].append(energy[i])


valid_energy = [e for e in energy if e >= 0]

total = sum(valid_energy)

summary = (total, len(energy))



if len(data["high"]) > 3:
    result = "Energy Waste Detected"

elif abs(len(data["efficient"]) - len(data["moderate"])) <= 1:
    result = "Efficient Campus"

elif total > 600:
    result = "Energy Waste Detected"

else:
    result = "Moderate Usage"


print("Efficient:", data["efficient"])
print("Moderate:", data["moderate"])
print("High:", data["high"])
print("Invalid:", data["invalid"])

print("Total Consumption:", summary[0])
print("Number of Buildings:", summary[1])

print("Efficiency Result:", result)
