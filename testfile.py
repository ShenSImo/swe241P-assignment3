from hw3 import *
import string
import time
import random
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

def test_normal():
    assert sortString("dcba", "merge") == "abcd"
    assert sortString("dcba", "quick") == "abcd"

def test_reverse_order():
    assert sortString("zyxwv", "merge") == "vwxyz"
    assert sortString("zyxwv", "quick") == "vwxyz"

def test_empty_string():
    assert sortString("", "merge") == ""
    assert sortString("", "quick") == ""

def test_compare_speed():
    word = "zxyabc" * 500

    start = time.perf_counter()
    sortString(word, "merge")
    merge_time = time.perf_counter() - start

    start = time.perf_counter()
    sortString(word, "quick")
    quick_time = time.perf_counter() - start

    print(f"Merge Sort: {merge_time:.6f}s")
    print(f"Quick Sort: {quick_time:.6f}s")