import random
import pandas as pd
import numpy as np
import math

def generate_data(n):
    data = []
    for i in range(n):
        record = {
            "zone": i + 1,
            "traffic": random.randint(0, 100),
            "air_quality": random.randint(0, 300),
            "energy": random.randint(0, 500)
        }
        data.append(record)
    return data

def classify_zone(t, aqi, e):
    if aqi > 200 or t > 80:
        return "High Risk"
    elif e > 400:
        return "Energy Critical"
    elif t < 30 and aqi < 100:
        return "Safe Zone"
    else:
        return "Moderate"

def calculate_risk(t, aqi, e):
    return t*0.4 + aqi*0.4 + e*0.2

def custom_sort(data):
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            if data[i]["traffic"] > data[j]["traffic"]:
                data[i], data[j] = data[j], data[i]
    return data

n = random.randint(15, 20)
data = generate_data(n)

reg = "AP24110011729"
num = int(reg[2:])

if num % 3 == 0:
    random.shuffle(data)
else:
    data = custom_sort(data)

for i in range(len(data)):
    t = data[i]["traffic"]
    aqi = data[i]["air_quality"]
    e = data[i]["energy"]
    data[i]["category"] = classify_zone(t, aqi, e)
    risk = calculate_risk(t, aqi, e)
    data[i]["risk_score"] = risk
    data[i]["risk_sqrt"] = math.sqrt(risk)

df = pd.DataFrame(data)

arr = df[["traffic", "air_quality", "energy"]].values
mean_values = np.mean(arr, axis=0)

top3 = df.nlargest(3, "risk_score")

max_risk = df["risk_score"].max()
avg_risk = df["risk_score"].mean()
min_risk = df["risk_score"].min()

summary = (max_risk, avg_risk, min_risk)

if max_risk > 250:
    decision = "Critical Emergency"
elif avg_risk > 180:
    decision = "High Alert"
elif avg_risk > 100:
    decision = "Moderate Risk"
else:
    decision = "City Stable"

print("\n--- CITY DATA ---")
print(df)

print("\n--- MEAN VALUES ---")
print("Traffic Mean:", mean_values[0])
print("Air Quality Mean:", mean_values[1])
print("Energy Mean:", mean_values[2])

print("\n--- TOP 3 RISK ZONES ---")
print(top3)

print("\n--- RISK SUMMARY ---")
print("Max Risk:", float(max_risk))
print("Average Risk:", float(avg_risk))
print("Min Risk:", float(min_risk))

print("\n--- FINAL DECISION ---")
print(decision)
