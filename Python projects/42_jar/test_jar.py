from jar import Jar
import pytest

def test_init():
    jar = Jar()
    jar.capacity == 12
    jar.size == 0

def test_init_invalid_capacity():
    with pytest.raises(ValueError):
        jar = Jar(-1)

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    assert jar.deposit(1) == 1
    assert jar.deposit(2) == 3
    assert jar.deposit(5) == 8
 
def test_deposit_invalid_value():
    jar = Jar()
    with pytest.raises(ValueError):
        jar.deposit(13)


def test_withdraw():
    jar = Jar()
    jar.deposit(12)
    assert jar.withdraw(1) == 11
    assert jar.withdraw(2) == 9
    assert jar.withdraw(5) == 4


def test_withdraw_invalid_value():
    jar = Jar()
    jar.deposit(10)
    with pytest.raises(ValueError):
        jar.withdraw(13)

