import math
class IrregularFraction(Exception):
    "Raised when input fraction is irregular"
    pass

    


def main():
    userFraction = fraction()
    userPercent = convert(userFraction)
    output = gauge(userPercent)
    print(output)


def fraction():
    while True:
        try:
            fuel = input("Fraction: ")
            fuel_fraction = list(fuel.split("/"))
            numerator = int(fuel_fraction[0])
            denominator = int(fuel_fraction[1])
            if numerator>denominator:
                raise IrregularFraction
            else:
                fraction = int(numerator)/int(denominator)
                return fraction
        except (ValueError, ZeroDivisionError, IrregularFraction):
            pass

def convert(fraction):
     percent = fraction*100
     return myround(percent)

def gauge(percent):
    if percent >= 99:
        return("F")
    elif percent <= 1:
         return("E")
    else:

        return (str(percent) + "%")

def myround(n):
    if n * 10 % 10 >= 5:
        return math.ceil(n)
    return math.floor(n)


if __name__ == "__main__":
    main()