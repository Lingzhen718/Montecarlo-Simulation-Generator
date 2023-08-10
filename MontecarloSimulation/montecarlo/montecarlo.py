import pandas as pd
import numpy as np
from collections import Counter

class Die:
    '''
    Simulates rolling a die with weighted sides.
    
    The DieSimulator class allows you to simulate rolling a die with weighted sides.
    A die has sides, or “faces”, and weights, and can be rolled to select a face.
    Each side contains a unique symbol. Symbols may be all alphabetic or all numeric.
    Normally, dice is “fair” meaning that the each side has an equal weight. An unfair die is one where the weights are unequal.

    The roll method generates random samples based on the weights.
    '''

    def __init__(self, faces):
        '''
        PURPOSE: Initialize a die object with a given list of faces
        
        INPUTS:
        faces      NumPy Array(Items in the array should be unique strings or numbers)      The faces of the die
        
        OUTPUTS:
        None

        NOTES:
        - The weights of each face (W) are initialized to 1
        - The weights with the faces are stored as die status
        '''
        if not isinstance(faces, np.ndarray):
            raise TypeError("Input die faces must be a NumPy array")
        if faces.dtype.kind not in ['S', 'i', 'u', 'f']:
            raise TypeError("Input die faces array must only contain strings or numbers")
        if len(np.unique(faces)) != len(faces):
            raise ValueError("Input die faces array must only contain unique values")
        self.faces = faces
        self.W = np.ones(len(faces))
        self._diedata = pd.DataFrame({'weights': self.W},index = self.faces)

    
    def changeweight(self, face, weight):
        '''
        PURPOSE: Change the weight of a face in the given die

        INPUTS:
        face      String or Numeric (Should be one of the value in face array)      The face to change the weight of
        weight    Numeric (Or castable as numeric; Cannot be negative)              The new weight of the face

        OUTPUTS:
        None

        NOTES:
        - The function will try to change the weight to be float type if the input is not numeric
        - Bothe the weight of the face (W) and the stored die status are changed
        '''
        if face not in self.faces:
            raise IndexError("Input face to change must in the original die faces array")
        if weight.isnumeric() == False:
            try:
                weight = float(weight)
            except:
                raise TypeError("Input weight to change must be a number")
        if weight < 0:
            raise TypeError("Input weight to change must be non-negative")
        self._diedata.loc[face] = weight
        self.W = self._diedata['weights'].values
    
    def rolldie(self, N=1):
        '''
        PURPOSE: Roll the die N times (one or more times) according to the given faces and weights (W), and return all the results in a list

        INPUTS:
        N      Integer (Default value is 1; Must be positive)      The number of times to roll the die

        OUTPUTS:
        results      List      The outcomes of all the N times die rolls

        NOTES:
        - The function does not store internally these results
        '''
        if isinstance(N, int) == False or N <= 0:
            raise TypeError("Input number of rolls must be an integer")
        self.result = list(np.random.choice(self.faces, N, p=self._diedata.weights/sum(self._diedata.weights)))
        return self.result
    
    def showdie(self):
        '''
        PURPOSE: Show the current status of the die

        INPUTS:
        None

        OUTPUTS:
        None

        NOTES:
        - The function prints the stored die status
        '''
        return self._diedata.copy()

class Game(Die):
    '''
    Simulates a game with multiple dice for multiple times.

    The Game class allows you to simulate a game consists of rolling of one or more similar dice (Die objects) one or more times.
    Similar dice means each die has the same number of sides and associated faces, but may have its own weights.
    Each game is initialized with a Python list that contains one or more dice.

    The play method plays the game by rolling each die M times.
    The showresults method shows the most recent play results in either wide or narrow form.
    '''

    def __init__(self, dies):
        '''
        PURPOSE: Initialize a game object with a given list of already instantiated similar dice
        
        INPUTS:
        dies      List (Must be instantiated die objects with similar dice)      The dies used for the game
        
        OUTPUTS:
        None
        
        NOTES:
        - This function do not check if the list actually contains Die objects with same faces
        - This function also initializes the results of the game in order to keep the results of most recent play
        '''
        self.dies = dies
        self._results = None
    
    def play(self, M):
        '''
        PURPOSE: Play the game by rolling each die M times

        INPUTS:
        M      Integer (Must be positive)      The number of times to roll each die

        OUTPUTS:
        None

        NOTES:
        - The function stores the results of the game
        '''
        if isinstance(M, int) == False or M <= 0:
            raise TypeError("Input number of rolls must be an integer")
        results = {}
        for index, die in enumerate(self.dies):
            result_onedie = die.rolldie(M)
            results[f'{index}'] = result_onedie
        self._results = pd.DataFrame(results)
        self._results.index = range(1, M+1)
        self._results.index.name = 'Roll Number'
        self._results.columns.name = 'Die Number'

    def showresults(self, form='wide'):
        '''
        PURPOSE: Show the results of the game in either wide or narrow form
        
        INPUTS:
        form      String (Must be either 'wide' or 'narrow')      The form of the results to show
        
        OUTPUTS:
        results      Pandas DataFrame      The results of the game in the given form

        NOTES:
        - The function returns the stored results of the game
        - The function raises error if the game has not been played yet
        - The function raises error if the input form is not 'wide' or 'narrow'
        '''
        if self._results is None:
            raise ValueError("The game has not been played yet")
        else:
            if form != 'wide' and form != 'narrow':
                raise ValueError("Input form option must be either 'wide' or 'narrow' in order to show the results")
            else:
                if form == 'wide':
                    return self._results.copy()
                if form == 'narrow':
                    return pd.DataFrame(self._results.copy().stack()).rename(columns={0:'Face'})

class Analyzer(Game):
    def __init__(self, games):
        '''
        PURPOSE: Initialize an analyzer object with a given game object
        
        INPUTS:
        games      Game object      The game to analyze
        
        OUTPUTS:
        None
        
        NOTES:
        - This function check if the input is a Game object, and if the game has been played
        - This function also initializes the gameover attribute in order to keep the results for use in later methods
        '''
        if not isinstance(games, Game):
            raise ValueError("Input must be a Game object.")
        if games._results is None:
            raise ValueError("The game has not been played yet")
        self.games = games
        self.gameover = self.games.showresults().copy()
    
    def jackpot(self):
        '''
        PURPOSE: Count the number of jackpots in the game
        
        INPUTS:
        None
        
        OUTPUTS:
        jackpot_count      Integer      The number of jackpots in the game
        
        NOTES:
        - The function first set the jackpot count to 0
        - Jackpot is defined as all the dice showing the same face in a roll
        '''
        self.jackpot_count = 0
        for i in range(1, len(self.gameover)+1):
            if all(m== self.gameover.loc[i][0] for m in self.gameover.loc[i]):
                self.jackpot_count += 1
        return self.jackpot_count
    
    def face_counts_per_roll(self):
        '''
        PURPOSE: Count the number of each face in each roll

        INPUTS:
        None

        OUTPUTS:
        face_count      Pandas DataFrame      The number of each face in each roll

        NOTES:
        - The data frame has an index of the roll number, face values as columns, and count values in the cells
        '''
        self.face_count = self.gameover.apply(lambda row: pd.Series([list(row).count(element) for element in self.games.dies[0].faces]), axis=1)
        self.face_count.columns = self.games.dies[0].faces
        self.face_count.index = self.gameover.index
        self.face_count.columns.name = 'Face'
        return self.face_count
    
    def combo_count(self):
        '''
        PURPOSE: Count the distinct and order-independent combinations of faces rolled, along with their counts
        
        INPUTS:
        None
        
        OUTPUTS:
        combo_count      Pandas DataFrame      The number of each combination of faces in the game
        
        NOTES:
        - The data frame has an multiIndex of distinct combinations and a column for the associated counts
        - The combinations are distinct in the sense that the order of the faces does not matter
        '''
        self.combo = dict(Counter(tuple(sorted(list(self.gameover.loc[i+1]), key=lambda x: str(x))) for i in range(len(self.gameover))))
        return pd.DataFrame(list(self.combo.values()), index=self.combo.keys(),columns=['count'])
    
    def permutation_count(self):
        '''
        PURPOSE: Count the distinct and order-dependent permutations of faces rolled, along with their counts

        INPUTS:
        None

        OUTPUTS:
        permutation_count      Pandas DataFrame      The number of each permutation of faces in the game

        NOTES:
        - The data frame has an multiIndex of distinct permutations and a column for the associated counts
        - The permutations are distinct in the sense that the order of the faces does matter
        '''
        self.permutation = dict(Counter(tuple(list(self.gameover.loc[i+1])) for i in range(len(self.gameover))))
        return pd.DataFrame(list(self.permutation.values()), index=self.permutation.keys(),columns=['count'])
