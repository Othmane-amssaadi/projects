import math

try:
    T = float(input("T (k) = "))
    lndea = ((-6009.5 / 8.314) * ((1 / T) - (1 / 273.15))) - ((37.87 / 8.314) * ((T - 273.15) / T) - (math.log(T / 273.15)))
    print("ln(alfa)=",-lndea)
    alfa = math.exp(lndea)
    print("activity est de ", alfa)
except:
    print("try again")
