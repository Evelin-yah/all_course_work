group_size = int(input())
days = int(input())

budget = 0
companions = group_size

for day in range(1, days + 1):
    if day % 10 == 0:
        companions -= 2
    if day % 15 == 0:
        companions += 5

    if day % 3 == 0:
        budget -= 3 * companions
    if day % 5 == 0:
        budget += 20 * companions
        if day % 3 == 0:
            budget -= 2 * companions

    budget += 50
    budget -= 2 * companions
coins_per_companion = int(budget / companions)

print(f"{companions} companions received {coins_per_companion} coins each.")
