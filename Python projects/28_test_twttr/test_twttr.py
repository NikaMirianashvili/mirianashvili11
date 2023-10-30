import twttr  

def main():
    test_ommit_vowels()


def test_ommit_vowels():
    assert twttr.ommit_vowels("salome") == "slm"
    assert twttr.ommit_vowels("What's your name?") == "Wht's yr nm?"
    assert twttr.ommit_vowels("CS50") == "CS50"
   

if __name__ == "__main__":
    main()