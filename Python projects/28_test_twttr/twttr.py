def main():
    txt  = input()
    onlyCons= ommit_vowels(txt)
    print(onlyCons)

def ommit_vowels(str):
    str_into_list = list(str.strip(" "))
    
    for index in range(len(str_into_list)):
        for j in ["a", "e", "i", "o", "u"]:
            if str_into_list[index] == j:
                str_into_list[index]= ""
            else: pass

    result = "".join(str_into_list)
    return result

if __name__ == "__main__":
    main()