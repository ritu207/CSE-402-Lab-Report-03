requests = [0,41,30,100,62,51,20]
head =70

total_movement = 0

print("Order:", head, end="")

for request in requests:
    total_movement += abs(request - head)
    head = request
    print(" ->", head, end="")

print("\nTotal Head Movement =", total_movement)

requests = [0,41,30,100,62,51,20]
head =70

requests.sort()

total_movement = 0

print("Order:", head, end="")

for request in requests:
    total_movement += abs(request - head)
    head = request
    print(" ->", head, end="")

print("\nTotal Head Movement =", total_movement)