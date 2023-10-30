# ROCK, PAPER, SCISSORS
#### Video Demo:  <https://youtu.be/bE_XhAjNopI>
#### Description:

## Beginning
I'm creating a software which will play "Rock, Paper, Scissors" with a user.
To do this I need:
1. user to be able to input their choice
2. computer generating random choice
3. outputting both choice
4. outputting winner

    ### rock, paper, scissors Rules

        * Rock beats Scissors
        * Paper beats Rock
        * Scissors beats Paper

## Advancements
to advance software I can add additional functions:
1. ask user after first game if they want to keep playing
2. quit game if they press anything other than Y
3. make game much more COMPLICATED by adding additional actions: Lizard and Spock


    ### rock, paper, scissors, lizard, Spock Rules

        * Rock beats Scissors
        * Rock beats Lizard
        * Paper beats Rock
        * Paper beats Spock
        * Scissors beats Paper
        * Scissors beats Lizard
        * Lizard beats Paper
        * Lizard beats Spock
        * Spock beats Rock
        * Spock beats Scissors

        <!-- for a better visualization check diagram: -->
        ![image](https://upload.wikimedia.org/wikipedia/en/c/cc/Rock_paper_scissors_lizard_spock.png)
4. count user's and computer's scores and display them after every game

## Coding Process
### beginning version 1.0
1. for the beginning version I only need one additional library: __Random__
    *   __Random__ for computer's random action
2. three different function
    * user_input() - which will get action and change it into 0, 1, or 2
    * computer_input() - which will generate random number 0, 1, or 2
    * match(user_input, computer_input) - function with two parameters to decide winner according to Rules

### advanced version
#### advanced version 2.0
1. for the advanced version I need to add library: __Re__
    * __Re__ for checking user's input and if it maches "Y" or "y" to exit game
2. while loop to keep playing until user exits on their choice

#### advanced version 2.1
1. because code will became way harder to read with additional actions, I'll add class __IntEnum__ from __enum__
    which will make code readable
2. I've split match(user_input, computer_input) function into two functions:
    * match_shoots_output(user_input, computer_input) - which outputs user's and computer's shoots
    * match_result(user_input, computer_input) - which match shoots and determines winner
this made code in my opinion easier to read

#### advanced version 2.2
1. the most important and hardest change - introducing dictionaries, so I won't have as much conditional sentences as I have right now in the match_result(user_input, computer_input) function.
beacuse when I'll add Lizard and Spock this function will become really hard to read.
__dict__ keys should be shoots which beats thier values.

2. __dict__ keys will be user_input. I'll make new variable where will be saved key's appropriate value
examp. {rock: scissors}
first we will see if there is a tie.
if not than:
if user chose rock, scissors will be saved in a new variable
if computer_input is equal to this new variable than user wins
else: computer_input is not neither rock nor scissors, than it is paper and computer wins

3. because I'm changing user's input into numbers, I've needed way to change them (and computer's output as well) into texts to print them so, user could see their and computer's choices and also final result, to do this I've created another funtion
   * index_to_text(index)

4. it's time to add additional shooting __Lizard__ and __Spock__ in the class, dict, user_input() and index_to_text() function's list. there is no need to change anything else.

#### advanced version 2.3
1. added counters - global variables and incrementing functions
    * increment_user_score() - increments global variable User_Score_Count
    * increment_computer_score() - increments global variable Computer_Score_Count
