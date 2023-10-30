import fuel
import pytest

def main():
    test_convert()
    test_gauge()
    test_passes_without_zeroDivisionError()
    test_passes_without_irregularFraction()


def test_convert():
    assert fuel.convert(1/5) == 20
    assert fuel.convert(1/7) == 14
    assert fuel.convert(1/8) == 13
    assert fuel.convert(1/9) == 11
    assert fuel.convert(2/23) == 9
 

def test_gauge():
    assert fuel.gauge(0.6) == "E"
    assert fuel.gauge(99.1) == "F"
    assert fuel.gauge(65) == "65%"
     
def test_passes_without_zeroDivisionError():
    with pytest.raises(Exception):
        fuel.convert(2/0)



if __name__ == "__main__":
    main()