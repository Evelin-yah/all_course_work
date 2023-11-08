number_of_snowballs = int(input())
value = 0
current_weight = 0
current_time = 0
current_quality = 0
for snowball in range(number_of_snowballs):
    weight = int(input())
    time = int(input())
    quality = int(input())

    current_value = (weight / time) ** quality
    if current_value > value:
        value = current_value
        current_weight = weight
        current_time = time
        current_quality = quality

print(f'{current_weight} : {current_time} = {int(value)} ({current_quality})')