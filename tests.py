import unittest
from functionsToTest import eat, nap


class ActivitiesToTest(unittest.TestCase):
    def test_eat_healthy(self):
        self.assertEqual(eat("broccoli", is_healthy=True),
                         "I'm eating broccoli because my body is a temple")

    def test_eat_unhealthy(self):
        self.assertEqual(eat("cheese", is_healthy=False),
                         "I'm eating cheese because it's not healthy")

    def test_short_nap(self):
        self.assertEqual(
            nap(1), f"Might need to snooze, I only slept for 1 hour, don't feel refreshed!")

    def test_long_nap(self):
        self.assertEqual(nap(3), "Feel refreshed because I slept for 3 hours!")


if __name__ == "__main__":
    unittest.main()
