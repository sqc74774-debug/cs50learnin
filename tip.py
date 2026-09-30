def dollar_to_float(cost):
    return float(cost.replace('$',''))
    
def percent_to_float(percentage):
    return float(percentage.replace('%',''))

def main():
    meal=dollar_to_float(input("How much was the meal?"))
    percentage=percent_to_float(input('What percentage would you like tip?'))
    tip=meal*percentage/100
    print("$",f"{tip:.2f}")
    

main()
    

