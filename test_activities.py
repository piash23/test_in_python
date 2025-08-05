import unittest
from activities import eat, nap

class ActivityTests(unittest.TestCase):
    def test_eat_healthy(self):
        """
        Eat should have a positive message for healthy eating.
        """
        self.assertEqual(
            eat("Broccoli", is_healthy=True),
            "I'm eating Broccoli, because my body is a temple",
        )

    def test_eat_unhealthy(self):
        """
        Eat should have a fun message for unhealthy eating.
        """
        self.assertEqual(
            eat("Pizza", is_healthy=False), "I'm eating Pizza, because YOLO!"
        )

    def test_short_nap(self):
        """
        Short naps should be refreshing.
        """
        self.assertEqual(nap(1), "I'm feeling refreshed after 1 hour of sleep.")

    def test_long_nap(self):
        """
        Long naps should be discouraging.
        """
        self.assertEqual(nap(3), "Ugh I overslept. I didn't mean to nap for 3 hours!")

if __name__ == "__main__":
    unittest.main()