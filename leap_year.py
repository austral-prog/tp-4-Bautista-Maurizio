def leap_year():
    def bisiesto():
        if (year % 4 == 0):
            print(f"El año {year} es bisiesto")
        else:
            print (f"El año {year} no es bisiesto")

    Year = input("Ingrese un año: ")
    year = int(Year)
    if (year %100==0):
        if (year % 4 == 0) and (year % 400 == 0):
             print(f"El año {year} es bisiesto")
        else:
            print (f"El año {year} no es bisiesto")
    else: bisiesto()
        
