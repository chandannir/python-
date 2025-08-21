items = {}
i = 0

while True:
    try:    
        grocery = input("").upper()
        if grocery not in items.values():
            items[i] = grocery
            i += 1
        else:
            continue
    except EOFError:
        for i, groceries in items.items():
            print(i, groceries)
        
        