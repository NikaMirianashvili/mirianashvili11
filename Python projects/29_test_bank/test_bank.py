import bank 

def main():
    test_greeting_fine()


def test_greeting_fine():
    assert bank.greeting_fine("Hello") == "$0"
    assert bank.greeting_fine("hello, dear customer") == "$0"
    assert bank.greeting_fine("hi there") == "$20"
    assert bank.greeting_fine("How can I help you?") == "$20"
    assert bank.greeting_fine("hope you feel amazing") == "$20"
    assert bank.greeting_fine("good morning") == "$100"
    assert bank.greeting_fine("Great to see you") == "$100"


if __name__ == "__main__":
    main()