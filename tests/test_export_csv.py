"""Checks that CSV exports preserve Unicode and neutralize formula cells."""

import csv
import io
import unittest

from export_csv import csv_bytes


class ExportTests(unittest.TestCase):
    def test_unicode_and_formula_like_text(self) -> None:
        rows = [
            {"position": "1", "text": "ខ្មែរ", "type": "Khmer span", "definition": "Khmer"},
            {"position": "8", "text": "=1+1", "type": "Other text", "definition": "—"},
        ]
        decoded = csv_bytes(rows).decode("utf-8-sig")
        exported = list(csv.DictReader(io.StringIO(decoded)))

        self.assertEqual(exported[0], rows[0])
        self.assertEqual(exported[1]["text"], "'=1+1")


if __name__ == "__main__":
    unittest.main()
