n, m = map(int, input().split(" "))
if n == 0:
    books = []
    box = 0
else:
    books = list(map(int, input().split(" ")))
    box = 1

weight = 0

for book in books:
    if weight + book > m:
        box += 1
        weight = book
    else:
        weight +=  book
    
        
print(box)