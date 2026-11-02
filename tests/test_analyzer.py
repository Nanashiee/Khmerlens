"""Behavior checks for the boundary splitter and exact glossary lookup."""

import unittest

from analyzer import analyze_text, load_glossary


class AnalyzerTests(unittest.TestCase):
    def setUp(self) -> None:
        self.glossary = {"សួស្តី": "hello", "ខ្មែរ": "Khmer"}

    def test_spaces_and_zero_width_spaces_are_explicit_boundaries(self) -> None:
        source = "សួស្តី ខ្មែរ\u200bសួស្តី"
        tokens = analyze_text(source, self.glossary)
        self.assertEqual([token.text for token in tokens], ["សួស្តី", "ខ្មែរ", "សួស្តី"])
        self.assertEqual([source[token.start:token.end] for token in tokens], [token.text for token in tokens])
        self.assertEqual([token.definition for token in tokens], ["hello", "Khmer", "hello"])

    def test_unbroken_khmer_is_not_claimed_as_separate_words(self) -> None:
        tokens = analyze_text("សួស្តីខ្មែរ", self.glossary)
        self.assertEqual(len(tokens), 1)
        self.assertEqual(tokens[0].kind, "Khmer span")
        self.assertIsNone(tokens[0].definition)

    def test_unknown_span_has_no_definition(self) -> None:
        tokens = analyze_text("មិនស្គាល់", self.glossary)
        self.assertEqual(tokens[0].text, "មិនស្គាល់")
        self.assertIsNone(tokens[0].definition)

    def test_punctuation_and_mixed_script_are_not_glossary_matches(self) -> None:
        tokens = analyze_text("សួស្តី! ABC ១២", self.glossary)
        self.assertEqual([token.kind for token in tokens], [
            "Khmer span", "Punctuation / symbol", "Other text", "Khmer span"
        ])
        self.assertEqual([token.definition for token in tokens], ["hello", None, None, None])

    def test_empty_and_whitespace_only_inputs(self) -> None:
        self.assertEqual(analyze_text("", self.glossary), [])
        self.assertEqual(analyze_text(" \n\u200b", self.glossary), [])

    def test_sample_glossary_loads(self) -> None:
        self.assertEqual(load_glossary()["អរគុណ"], "thank you")


if __name__ == "__main__":
    unittest.main()
