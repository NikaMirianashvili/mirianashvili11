def main():
     number = get_number()
     meow(number)

def meow(n):
     for _ in range(n):
        print("meow")


def get_number():
    while True:
       n = int(input("what is n? :"))
       if n < 0:
          print("Invalid Number")
          break
    return n
main()
