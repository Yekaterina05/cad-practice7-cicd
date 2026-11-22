import unittest
from app import response_for


class AppTests(unittest.TestCase):
    def test_health(self):
        status, body = response_for("/health")
        self.assertEqual(status, 200)
        self.assertEqual(body["status"], "broken")

    def test_home(self):
        status, body = response_for("/")
        self.assertEqual(status, 200)
        self.assertEqual(body["student"], "Yekaterina Pyurko")
        self.assertIn("version", body)

    def test_unknown_path(self):
        status, body = response_for("/missing")
        self.assertEqual(status, 404)
        self.assertEqual(body["error"], "Not found")


if __name__ == "__main__":
    unittest.main()
