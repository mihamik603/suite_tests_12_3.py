import unittest
from tests_12_3 import RunnerTest, TournamentTest

test_suite = unittest.TestSuite()
test_suite.addTest(unittest.makeSuite(RunnerTest))
test_suite.addTest(unittest.makeSuite(TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(test_suite)
