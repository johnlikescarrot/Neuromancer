import unittest
from unittest.mock import patch

from scripts.translate_novel import translate_batch


class TranslationSafetyTests(unittest.TestCase):
    @patch("scripts.translate_novel.time.sleep")
    @patch("scripts.translate_novel.urllib.request.urlopen", side_effect=OSError("offline"))
    def test_failed_translation_never_returns_source_as_translation(self, _urlopen, _sleep):
        with self.assertRaisesRegex(RuntimeError, "Translation failed"):
            translate_batch(["An English sentence."])


if __name__ == "__main__":
    unittest.main()
