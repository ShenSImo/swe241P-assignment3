from hw3 import *

# test many duplicate letters
def test_duplicates():
    word = "a" * 2000
    assert sortString(word, "merge") == word
    assert sortString(word, "quick") == word

    word = "ba" * 1000
    answer = "a" * 1000 + "b" * 1000
    assert sortString(word, "merge") == answer
    assert sortString(word, "quick") == answer

    print("test_duplicates passed")