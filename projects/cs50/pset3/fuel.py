
def fuel_gauge():
    while True:
        fraction = input("Fraction: ").split("/")
        try:
            if len(fraction) == 2:
                numerator = int(fraction[0])
                denominator = int(fraction[1])
            else:
                continue
            
            fuel_amount = (numerator / denominator) * 100
            
            if fuel_amount < 0:
                raise ValueError
            elif fuel_amount >= 99:
                print("F") 
            elif fuel_amount <=1:
                print("E")
            else:
                print(f"{round(fuel_amount)}")
        
        except ZeroDivisionError:
            print("You cannot divide by zero!")
            continue
        except ValueError:
            print("Unable to Divide!")
            continue
            
fuel_gauge()
