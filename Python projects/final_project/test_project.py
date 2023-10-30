import project

def main():
    test_user_input_encrypt()
    test_computer_input()
    test_index_to_text()
    test_tie_match_result()
    test_win_match_result()
    test_lose_match_result()

def test_user_input_encrypt():
    assert project.user_input_encrypt("rock") == project.Shoot.Rock
    assert project.user_input_encrypt("Rock") == project.Shoot.Rock
    assert project.user_input_encrypt("RoCk") == project.Shoot.Rock
    assert project.user_input_encrypt("Lizard") == project.Shoot.Lizard
    assert project.user_input_encrypt("LIZARD") == project.Shoot.Lizard
    assert project.user_input_encrypt("SPock") == project.Shoot.Spock
    
def test_computer_input():
    assert project.computer_input() in [0, 1, 2, 3, 4]

def test_index_to_text():
    assert project.index_to_text(0) == "Rock"
    assert project.index_to_text(1) == "Paper"
    assert project.index_to_text(2) == "Scissors"
    assert project.index_to_text(3) == "Lizard"
    assert project.index_to_text(4) == "Spock"

def test_tie_match_result():
    assert project.match_result(project.Shoot.Rock, project.Shoot.Rock) == "It's a tie"
    assert project.match_result(project.Shoot.Paper, project.Shoot.Paper) == "It's a tie"
    assert project.match_result(project.Shoot.Scissors, project.Shoot.Scissors) == "It's a tie"
    assert project.match_result(project.Shoot.Lizard, project.Shoot.Lizard) == "It's a tie"
    assert project.match_result(project.Shoot.Spock, project.Shoot.Spock) == "It's a tie"

def test_win_match_result():
    assert project.match_result(project.Shoot.Rock, project.Shoot.Scissors) == "You Won!, Rock beats Scissors"
    assert project.match_result(project.Shoot.Rock, project.Shoot.Lizard) == "You Won!, Rock beats Lizard"
    assert project.match_result(project.Shoot.Paper, project.Shoot.Rock) == "You Won!, Paper beats Rock"
    assert project.match_result(project.Shoot.Paper, project.Shoot.Spock) == "You Won!, Paper beats Spock"
    assert project.match_result(project.Shoot.Scissors, project.Shoot.Paper) == "You Won!, Scissors beats Paper"
    assert project.match_result(project.Shoot.Scissors, project.Shoot.Lizard) == "You Won!, Scissors beats Lizard"
    assert project.match_result(project.Shoot.Lizard, project.Shoot.Paper) == "You Won!, Lizard beats Paper"
    assert project.match_result(project.Shoot.Lizard, project.Shoot.Spock) == "You Won!, Lizard beats Spock"
    assert project.match_result(project.Shoot.Spock, project.Shoot.Rock) == "You Won!, Spock beats Rock"
    assert project.match_result(project.Shoot.Spock, project.Shoot.Scissors) == "You Won!, Spock beats Scissors"

def test_lose_match_result():
    assert project.match_result(project.Shoot.Scissors, project.Shoot.Rock) == "You Lost, Rock beats Scissors"
    assert project.match_result(project.Shoot.Lizard, project.Shoot.Rock) == "You Lost, Rock beats Lizard"
    assert project.match_result(project.Shoot.Rock, project.Shoot.Paper) == "You Lost, Paper beats Rock"
    assert project.match_result(project.Shoot.Spock, project.Shoot.Paper) == "You Lost, Paper beats Spock"
    assert project.match_result(project.Shoot.Paper, project.Shoot.Scissors) == "You Lost, Scissors beats Paper"
    assert project.match_result(project.Shoot.Lizard, project.Shoot.Scissors) == "You Lost, Scissors beats Lizard"
    assert project.match_result(project.Shoot.Paper, project.Shoot.Lizard) == "You Lost, Lizard beats Paper"
    assert project.match_result(project.Shoot.Spock, project.Shoot.Lizard) == "You Lost, Lizard beats Spock"
    assert project.match_result(project.Shoot.Rock, project.Shoot.Spock) == "You Lost, Spock beats Rock"
    assert project.match_result(project.Shoot.Scissors, project.Shoot.Spock) == "You Lost, Spock beats Scissors"


if __name__ == "__main__":
    main()