from montecarlo import Die, Game, Analyzer
import unittest
import numpy as np
import pandas as pd

class TestDie(unittest.TestCase):
    def test_changeweight(self):
        face1 = np.array([1,2,3,4,5,6])
        die1 = Die(face1)
        die1.changeweight(6, 5)
        message1 = "The weight of face has not been changed"
        self.assertEqual(die1.W[5], 5, message1)
    
    def test_rolldie(self):
        face2 = np.array([1,2,3,4,5,6])
        die2 = Die(face2)
        die2.rolldie(2)
        message2 = "The result of die is not in the faces"
        self.assertIn(die2.result[1], die2.faces, message2)

    def test_showdie(self):
        face3 = np.array([1,2,3,4,5,6])
        die3 = Die(face3)
        message3 = "The status of die is not shown"
        self.assertIn(len(die3.showdie()), 6, message3)
    
if __name__ == '__main__':
    unittest.main(verbosity=3)
    
class TestGame(unittest.TestCase):
    def test_play(self):
        face4 = np.array([1,2,3,4,5,6])
        die4 = Die(face4)
        die5 = Die(face4)
        die5.changeweight(6, 5)
        dies1 = [die4, die5]
        game1 = Game(dies1)
        game1.play(5)
        expected = (5,2)
        message4 = "The game is not played"
        self.assertEqual(game1.showresults().shape, expected, message4)
    
    def test_showresults(self):
        face5 = np.array([1,2,3,4,5,6])
        die6 = Die(face5)
        die7 = Die(face5)
        dies2 = [die6, die7]
        game2 = Game(dies2)
        game2.play(5)
        expected = (5,2)
        message5 = "The game is not played"
        self.assertEqual(game2.showresults().shape, expected, message5)

if __name__ == '__main__':
    unittest.main(verbosity=3)

class TestAnalyzer(unittest.TestCase):
    def test_jackpot(self):
        face6 = np.array([1,2,3,4,5,6])
        die8 = Die(face6)
        die9 = Die(face6)
        dies3 = [die8, die9]
        game3 = Game(dies3)
        game3.play(5)
        analyzer1 = Analyzer(game3)
        ajresult = analyzer1.jackpot()
        ajresult1 = isinstance(ajresult, int)
        message6 = "The jackpot is not calculated"
        self.assertTrue(ajresult1, message6)

    def test_face_counts_per_roll(self):
        face7 = np.array([1,2,3,4,5,6])
        die10 = Die(face7)
        die11 = Die(face7)
        dies4 = [die10, die11]
        game4 = Game(dies4)
        game4.play(5)
        analyzer2 = Analyzer(game4)
        face_counts = analyzer2.face_counts_per_roll()
        message7 = "The face counts per roll is not calculated"
        self.assertEqual(face_counts.shape, (5,6), message7)
    
    def test_combo_count(self):
        face8 = np.array([1,2,3,4,5,6])
        die12 = Die(face8)
        die13 = Die(face8)
        dies5 = [die12, die13]
        game5 = Game(dies5)
        game5.play(5)
        analyzer3 = Analyzer(game5)
        combo_count1 = analyzer3.combo_count()
        combo_count2 = isinstance(combo_count1, pd.DataFrame)
        message8 = "The combo count is not calculated"
        self.assertTrue(combo_count2, message8)

    def test_permutation_count(self):
        face9 = np.array([1,2,3,4,5,6])
        die14 = Die(face9)
        die15 = Die(face9)
        dies6 = [die14, die15]
        game6 = Game(dies6)
        game6.play(5)
        analyzer4 = Analyzer(game6)
        permutation_count1 = analyzer4.permutation_count()
        permutation_count2 = isinstance(permutation_count1, pd.DataFrame)
        message9 = "The permutation count is not calculated"
        self.assertTrue(permutation_count2, message9)
    
if __name__ == '__main__':
    unittest.main(verbosity=3)