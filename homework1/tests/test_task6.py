from task6 import how_many_words_in_file
from pathlib import Path

def test_task6_file_word_count():
    assert how_many_words_in_file() == 104
