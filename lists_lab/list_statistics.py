n = int(input())

positives = []
negatives =[]

for num in range(n):
    current_num = int(input())
    if current_num < 0:
        negatives.append(current_num)
    else:
        positives.append(current_num)

print(positives)
print(negatives)
print(f"Count of positives: {len(positives)} \nSum of negatives: {sum(negatives)}")