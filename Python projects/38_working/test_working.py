import working
import pytest


def main():
    test_general_time()
    test_convert()
    test_invalid_time()
    test_invalid_space()



def test_general_time():
    assert working.general_time("AM", 12, 30) == "00:30"
    assert working.general_time("AM", 3, 30) == "03:30"
    assert working.general_time("AM", 11, None) == "11:00"
    assert working.general_time("PM", 12, 30) == "12:30"
    assert working.general_time("PM", 4, 30) == "16:30"
    assert working.general_time("PM", 8, None) == "20:00"

def test_convert():
    assert working.convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert working.convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert working.convert("10 PM to 8 AM") == "22:00 to 08:00"
    assert working.convert("10:30 PM to 8:50 AM") == "22:30 to 08:50"
 
def test_invalid_time():
    with pytest.raises(ValueError):
        working.convert("13:00 AM - 2:00 PM")

def test_invalid_space():
    with pytest.raises(ValueError):
        working.convert("13:00AM to 2:00PM")

if __name__ == "__main__":
    main()