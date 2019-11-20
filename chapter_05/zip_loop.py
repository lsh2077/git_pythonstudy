names = ['a','b','c']
scores = [9,4,3]

for k in range(len(names)):
    print(names[k],scores[k])

print()
for name, score in zip(names,scores):
    print(name,score)