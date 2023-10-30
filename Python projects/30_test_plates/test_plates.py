import plates

def main():
    test_length()
    test_number_place() 
    test_nofirst_zeros()



def test_length():
    assert plates.is_valid("sa") == True
    assert plates.is_valid("sal") == True
    assert plates.is_valid("salo") == True
    assert plates.is_valid("salom") == True
    assert plates.is_valid("salome") == True


def test_number_place():

    assert plates.is_valid("ww1") == True
    assert plates.is_valid("ww12") == True
    assert plates.is_valid("www5") == True
    assert plates.is_valid("www99") == True
    assert plates.is_valid("wwww6") == True
    assert plates.is_valid("wwwww3") == True

def test_nofirst_zeros():
    assert plates.is_valid("www90") == True
    assert plates.is_valid("ww60") == True
    assert plates.is_valid("wwww30") == True




if __name__ == "__main__":
    main()