with open('data.txt') as f:
    contents = f.read().split()

# o2
olist = contents
i = 0
while len(olist) > 1:
    common = [str(int(sum([int(j[i]) for j in olist]) >= len(olist)/2)) for i in range(len(olist[0]))]
    olist = [o for o in olist if o[i] == common[i]]
    i += 1

# co2
clist = contents
i = 0
while len(clist) > 1:
    nommon = [str(int(sum([int(j[i]) for j in clist]) < len(clist)/2)) for i in range(len(clist[0]))]
    clist = [c for c in clist if c[i] == nommon[i]]
    i += 1

print(int(olist[0], 2) * int(clist[0], 2))