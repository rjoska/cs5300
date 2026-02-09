from task6 import how_many_words_in_file
from pathlib import Path

# A single test to ensure the number of words is 104 (Maybe more tests should be added such as getting the filepath?)
def test_task6_file_word_count():
    assert how_many_words_in_file() == 104
