import numb3rs

def main():
    test_characters()
    test_number_values()


def test_characters():
    assert numb3rs.validate("cat") == False
    assert numb3rs.validate("cat.dog.tea.cup") == False
    assert numb3rs.validate(".0.0.0") == False
    assert numb3rs.validate("0.0.0.0") == True

def test_number_values():
    assert numb3rs.validate("127.0.0.1") == True
    assert numb3rs.validate("255.255.255.255") == True
    assert numb3rs.validate("512.512.512.512") == False
    assert numb3rs.validate("1.2.3.1000") == False



if __name__ == "__main__":
    main()