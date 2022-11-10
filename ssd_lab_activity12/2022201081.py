from datetime import datetime


format = "%H:%M:%S.%f"

f = open("./file.txt")

l = []

lines = f.readlines()


for i in lines:
    l.append(i.split("\t"))

c1 = 0
t1 = ""
r1 = 0


temp_counter = 0
r_count = 0
fg = False
for i in l:
    if (i[0] == "\n"):
        temp_counter = 0
        continue
    else:
        for j in range(1, len(i)):
            if (i[j] != "0" and i[j] != "\n"):
                
                r1 = temp_counter
                c1 = j
                fg = True
                break
        if (fg):
            t1 = i[0]
            break
        temp_counter += 1
    r_count += 1

for i in l[r_count:]:
    if (i[0] != "\n"):
        r_count += 1
    else:
        break

r2 = 0
t2 = ""
for i in l[r_count:]:
    if (i[0] == "\n"):
        temp_counter = 0
        continue
    else:
        if (i[c1] != "0" and temp_counter < r1):
            r2 = temp_counter
            t2 = i[0]
            break
        temp_counter += 1

print(" Length of stride : {}".format(r1-r2))


t2 = datetime.strptime(t2, format)
t1 = datetime.strptime(t1, format)

velocity = (r1 - r2) / (t2 - t1).total_seconds()
print("Stride Velocity: {}".format(velocity))

steps = (2/abs(t2 - t1).total_seconds())*60
print("Cadence: {}".format(steps))

f.close()
