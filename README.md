# Montecarlo Simulation Generator

***This is the Final Project for DS5100***

## METADATA

Name: Lingzhen Zhu

Project Name: Montecarlo Simulator

## SYNOPSIS

You can install the package using this command:
pip install -e .
(pandas and numpy install are needed)

* You can import the package using these commands:
from MontecarloSimulation.montecarlo import Die
from MontecarloSimulation.montecarlo import Game
from MontecarloSimulation.montecarlo import Analyzer

* To create a die object, you can use this commands:
die1 = Die(np.array([1, 2, 3, 4, 5, 6]))
die1.changeweight(6, 3)
die1.rolldie(5)
die1.showdie()

* To create a game object, you can use this commands:
die2 = Die(np.array([1, 2, 3, 4, 5, 6]))
game1 = Game([die1, die2])
game1.play(5)
game1.showresults('narrow')

* To create a analyzer object, you can use this commands:
analyzer1 = Analyzer(game1)
analyzer1.jackpot()
analyzer1.face_counts_per_roll()
analyzer1.combo_count()
analyzer1.permutation_count()


## API DESCRIPTION

See INPUTS and OUTPUTS under each class and function for descriptions of parameters and return values.

Class
* Die
* Game
* Analyzer

     |  Class Game(Die)
     |  Game(dies)
     |  
     |  Simulates a game with multiple dice for multiple times.
     |  
     |  The Game class allows you to simulate a game consists of rolling of one or more similar dice (Die objects) one or more times.
     |  Similar dice means each die has the same number of sides and associated faces, but may have its own weights.
     |  Each game is initialized with a Python list that contains one or more dice.
     |  
     |  The play method plays the game by rolling each die M times.
     |  The showresults method shows the most recent play results in either wide or narrow form.
     |  
     |  Method resolution order:
     |      Game
     |      Die
     |      builtins.object
     |  
     |  Methods defined here:
     |  
     |  __init__(self, dies)
     |      PURPOSE: Initialize a game object with a given list of already instantiated similar dice
     |      
     |      INPUTS:
     |      dies      List (Must be instantiated die objects with similar dice)      The dies used for the game
     |      
     |      OUTPUTS:
     |      None
     |      
     |      NOTES:
     |      - This function do not check if the list actually contains Die objects with same faces
     |      - This function also initializes the results of the game in order to keep the results of most recent play
     |  
     |  play(self, M)
     |      PURPOSE: Play the game by rolling each die M times
     |      
     |      INPUTS:
     |      M      Integer (Must be positive)      The number of times to roll each die
     |      
     |      OUTPUTS:
     |      None
     |      
     |      NOTES:
     |      - The function stores the results of the game
     |  
     |  showresults(self, form='wide')
     |      PURPOSE: Show the results of the game in either wide or narrow form
     |      
     |      INPUTS:
     |      form      String (Must be either 'wide' or 'narrow')      The form of the results to show
     |      
     |      OUTPUTS:
     |      results      Pandas DataFrame      The results of the game in the given form
     |      
     |      NOTES:
     |      - The function returns the stored results of the game
     |      - The function raises error if the game has not been played yet
     |      - The function raises error if the input form is not 'wide' or 'narrow'
     |  
     |  ----------------------------------------------------------------------
      class Analyzer(Game)
     |  Analyzer(games)
     |   Analyzes the results of a game.
     |  The Analyzer class allows you to analyze the results of a game.
     |   The game must be played first before the analysis.
     |   The jackpot and face counts per roll method statistically record the occurrence of each face of the die according to             |    certain rules
     |   The combo count and permutation count method statistically record the combination of all the faces
    
     |  Methods defined here:
     |  
     |  __init__(self, games)
     |      PURPOSE: Initialize an analyzer object with a given game object
     |      
     |      INPUTS:
     |      games      Game object      The game to analyze
     |      
     |      OUTPUTS:
     |      None
     |      
     |      NOTES:
     |      - This function check if the input is a Game object, and if the game has been played
     |      - This function also initializes the gameover attribute in order to keep the results for use in later methods
     |  
     |  combo_count(self)
     |      PURPOSE: Count the distinct and order-independent combinations of faces rolled, along with their counts
     |      
     |      INPUTS:
     |      None
     |      
     |      OUTPUTS:
     |      combo_count      Pandas DataFrame      The number of each combination of faces in the game
     |      
     |      NOTES:
     |      - The data frame has an multiIndex of distinct combinations and a column for the associated counts
     |      - The combinations are distinct in the sense that the order of the faces does not matter
     |  
     |  face_counts_per_roll(self)
     |      PURPOSE: Count the number of each face in each roll
     |      
     |      INPUTS:
     |      None
     |      
     |      OUTPUTS:
     |      face_count      Pandas DataFrame      The number of each face in each roll
     |      
     |      NOTES:
     |      - The data frame has an index of the roll number, face values as columns, and count values in the cells
     |  
     |  jackpot(self)
     |      PURPOSE: Count the number of jackpots in the game
     |      
     |      INPUTS:
     |      None
     |      
     |      OUTPUTS:
     |      jackpot_count      Integer      The number of jackpots in the game
     |      
     |      NOTES:
     |      - The function first set the jackpot count to 0
     |      - Jackpot is defined as all the dice showing the same face in a roll
     |  
     |  permutation_count(self)
     |      PURPOSE: Count the distinct and order-dependent permutations of faces rolled, along with their counts
     |      
     |      INPUTS:
     |      None
     |      
     |      OUTPUTS:
     |      permutation_count      Pandas DataFrame      The number of each permutation of faces in the game
     |      
     |      NOTES:
     |      - The data frame has an multiIndex of distinct permutations and a column for the associated counts
     |      - The permutations are distinct in the sense that the order of the faces does matter
     |  
       
## MANIFEST
MontecarloSimulation
*montecarlo
     __init__.py

     montecarlo.py

*montecarlo_demo.ipynb
*montecarlo_test_results.txt
*setup.py


***Thank you!***
