requests = [0,41,30,100,62,51,20]
head =70

total = 0

left =[]
right =[]

for r in requests :
  if r < head :
    left.append(r)
  else:
    right.append(r)

left.sort(reverse = True)

right.sort()

print("Order :" ,head ,end = "")

for r in left :
  total += abs(head -r)
  head = r
  print("->", head ,end = " ")

if head != 0 :
  total += head
  head = 0
  print("->", head ,end = " ")

for r in right :
  total += abs(head -r)
  head = r
  print("->", head ,end = " ")

print("\nTotal Head Movement = " , total)

requests = [0,41,30,100,62,51,20]
head =70

total = 0

left =[]
right =[]

for r in requests :
  if r < head :
    left.append(r)
  else:
    right.append(r)

left.sort(reverse = True)

right.sort()

print("Order :" ,head ,end = "")

for r in right :
  total += abs(head -r)
  head = r
  print("->", head ,end = " ")

if head != 100 :
  total += 100 - head
  head = 100
  print("->", head ,end = " ")

for r in left :
  total += abs(head -r)
  head = r
  print("->", head ,end = " ")

print("\nTotal Head Movement = " , total)