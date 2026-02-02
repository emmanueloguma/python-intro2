combs = []
for x in [1,3,2]:
    for y in [1,4,3]:
        if x != y:
            combs.append((x, y))
            
print(combs)