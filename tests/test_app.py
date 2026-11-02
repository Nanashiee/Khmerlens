"""A small end-to-end check of the Streamlit results view."""

import unittest
from pathlib import Path

from streamlit.testing.v1 import AppTest


APP_PATH = Path(__file__).resolve().parents[1] / "app.py"


class AppTests(unittest.TestCase):
    def test_sample_input_shows_glossary_results(self) -> None:
        app = AppTest.from_file(str(APP_PATH)).run(timeout=20)
        app.text_area[0].set_value("សួស្តី ខ្មែរ").run(timeout=20)

        self.assertEqual(list(app.exception), [])
        self.assertEqual(len(app.dataframe), 1)
        self.assertTrue(any("2 Khmer spans" in item.value for item in app.get("markdown")))


if __name__ == "__main__":
    unittest.main()
