import um

def main():
    test_count_separate_ums()
    test_dont_count_word_ums()
    test_capital_letters()

def test_count_separate_ums():
    assert um.count("um") == 1
    assert um.count("um?") == 1
    assert um.count("um...") == 1
    assert um.count("hello, um, world") == 1
    assert um.count("um, hello, um, world") == 2
    assert um.count("um, thanks for the album.") == 1
    assert um.count("um, thanks, um...") == 2 

def test_dont_count_word_ums():
    assert um.count("yummy") == 0
    assert um.count("um, can you hold my umbrella?") == 1
    assert um.count("um, thanks for the album.") == 1

def test_capital_letters():
    assert um.count("Um") == 1
    assert um.count("UM?") == 1
    assert um.count("uM...") == 1
    assert um.count("hello, Um, world") == 1
    assert um.count("Um, hello, um, world") == 2
    assert um.count("UM, thanks for the albuM.") == 1


if __name__=="__main__":
    main()