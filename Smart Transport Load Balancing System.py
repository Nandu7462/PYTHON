n = int(input("enter no of weights"))
weights = [0] * n

for i in range(n):
    weights[i] = int(input("enter weight"))

very_light = [0]*n
normal_load = [0]*n
heavy_load = [0]*n
overload = [0]*n
invalid_entries = [0]*n

vl = 0
nl = 0
hl = 0
ol = 0
ie = 0

valid_count = 0

for i in  range(n):
    if weights[i]  < 0:
        invalid_entries[ie] = weights[i]
        ie += 1

    elif weights[i] >= 0 and weights[i] <=5 :
        very_light[vl] = weights[i]
        vl += 1
        valid_count += 1

    elif weights[i] >= 6 and weights[i] <= 25:
         normal_load[nl] = weights[i]
         nl += 1
         valid_count += 1

    elif weights[i] >= 26 and weights[i] <=60:
        heavy_load[hl] = weights[i]
        hl += 1
        valid_count += 1

    elif weights[i] > 60:
        overload[ol] = weights[i]
        ol += 1
        valid_count += 1


# Personalization values
str ="ANANDGOKULKOTA"
L = len(str)
print(L)
PLI = L % 3

affected = 0

# Rule C → Keep only Normal and Heavy

affected = vl + ol + ie

vl = 0
ol = 0
ie = 0


# Output

print("L value:", L)
print("PLI value:", PLI)
print("Applied Rule: Rule C")

print("Final Normal Load:", normal_load[:nl])
print("Final Heavy Load:", heavy_load[:hl])

print("Total Valid Weights:", valid_count)
print("Affected Items:", affected)


