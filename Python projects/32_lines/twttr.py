def main():
    txt  = input()
    ommit_vowels(txt)

#this function removes vowels from every string
def ommit_vowels(str):
    str_into_list = list(str.strip(" "))
 
    for index in range(len(str_into_list)):
        for j in ["a", "e", "i", "o", "u"]:
            if str_into_list[index] == j:
                str_into_list[index]= ""
            else: pass


    print("".join(str_into_list))

if __name__ == "__main__":
    main()