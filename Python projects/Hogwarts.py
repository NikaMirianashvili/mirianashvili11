class IrregularFraction(Exception):
    "Raised when input fraction is irregular"
    pass


def main():
    output(fraction())

def fraction():
    while True:
        try:
            x = input("Fraction: ")
            fuel_fraction = list(x.split("/"))
            regenerator = int(fuel_fraction[0])
            degenerator = int(fuel_fraction[1])
            if regenerator>degenerator:
                    raise IrregularFraction
            else:
                    fraction = int(fuel_fraction[0]) / int(fuel_fraction[1])
                    return fraction

        except (ValueError, ZeroDivisionError, IrregularFraction):
            pass
        else:
             break

def output(fraction):
     pc = fraction*100
     if pc >= 99:
          print("F")
     elif pc <= 1:
          print("E")
     else:
          print(round(pc), "%")

main()





