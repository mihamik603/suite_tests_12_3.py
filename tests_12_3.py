import unittest
from functools import wraps

def skip_if_frozen(test_case):
    @wraps(test_case)
    def wrapper(self, *args, **kwargs):
        if self.is_frozen:
            self.skipTest('Тесты в этом кейсе заморожены')
        return test_case(self, *args, **kwargs)
    return wrapper

class Runner:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

    def __eq__(self, other):
        if isinstance(other, Runner):
            return self.name == other.name
        return False

    def run(self, distance):
        time = distance / self.speed
        return time

    def walk(self, distance):
        time = distance / (self.speed / 2)
        return time

class Tournament:
    def __init__(self, distance, participants):
        self.distance = distance
        self.participants = participants

    def start(self):
        results = {}
        for runner in self.participants:
            time_taken = runner.run(self.distance)
            results[time_taken] = runner.name
        return dict(sorted(results.items()))

class RunnerTest(unittest.TestCase):
    is_frozen = False

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner1 = Runner("Usain", 10)
        self.runner2 = Runner("Andrey", 9)
        self.runner3 = Runner("Nick", 3)

    @classmethod
    def tearDownClass(cls):
        for result in cls.all_results.values():
            print(result)

    @skip_if_frozen
    def test_run(self):
        self.assertEqual(self.runner1.run(100), 10)
        self.assertEqual(self.runner2.run(90), 10)

    @skip_if_frozen
    def test_walk(self):
        self.assertEqual(self.runner1.walk(100), 20)
        self.assertEqual(self.runner2.walk(90), 20)

class TournamentTest(unittest.TestCase):
    is_frozen = True  # Установлено в True для пропуска тестов

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner1 = Runner(name="Усэйн", speed=10)
        self.runner2 = Runner(name="Андрей", speed=9)
        self.runner3 = Runner(name="Ник", speed=3)

    @classmethod
    def tearDownClass(cls):
        for key, value in cls.all_results.items():
            print(f"{key}: {value}")

    @skip_if_frozen
    def test_race_usain_nick(self):
        tournament = Tournament(distance=90, participants=[self.runner1, self.runner3])
        self.all_results.update(tournament.start())
        self.assertTrue(self.all_results[max(self.all_results)] == "Ник")

    @skip_if_frozen
    def test_race_andrey_nick(self):
        tournament = Tournament(distance=90, participants=[self.runner2, self.runner3])
        self.all_results.update(tournament.start())
        self.assertTrue(self.all_results[max(self.all_results)] == "Ник")

    @skip_if_frozen
    def test_race_usain_andrey_nick(self):
        tournament = Tournament(distance=90, participants=[self.runner1, self.runner2, self.runner3])
        self.all_results.update(tournament.start())
        self.assertTrue(self.all_results[max(self.all_results)] == "Ник")

if __name__ == '__main__':
    unittest.main()
