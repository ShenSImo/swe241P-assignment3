from hw3 import *
# ===================== Test Cases =====================

def test_sortString():
    # (输入, 预期输出)
    cases = [
        ("rat", "art"),          # 普通单词
        ("mango", "agmno"),      # 题目里的例子
        ("ogtan", "agnot"),      # 题目里的例子
        ("bucket", "bcektu"),    # 题目里的例子
        ("", ""),                # 空字符串
        ("a", "a"),              # 只有一个字母
        ("aaa", "aaa"),          # 全部相同
        ("banana", "aaabnn"),    # 有重复字母
        ("abcd", "abcd"),        # 已经排好序
        ("dcba", "abcd"),        # 完全倒序
        ("Happy", "Happy"),      # 大写在小写前面（'H'=72 < 'a'=97）
        ("Tar", "Tar"),          # 'T'=84 < 'a'=97 < 'r'=114
    ]
    for algorithm in ["merge", "quick"]:
        for s, expected in cases:
            result = sortString(s, algorithm)
            assert result == expected, f"{algorithm}: sortString({s!r}) = {result!r}, expected {expected!r}"
    print("test_sortString passed ✅")


def test_groupAnagram():
    # 1. 题目给的例子
    assert groupAnagram(["bucket", "rat", "mango", "tango", "ogtan", "tar"]) == \
        [["bucket"], ["rat", "tar"], ["mango"], ["tango", "ogtan"]]

    # 2. 空列表
    assert groupAnagram([]) == []

    # 3. 只有一个单词
    assert groupAnagram(["abc"]) == [["abc"]]

    # 4. 完全没有 anagram
    assert groupAnagram(["abc", "def", "ghi"]) == [["abc"], ["def"], ["ghi"]]

    # 5. 所有单词都是同一组
    assert groupAnagram(["listen", "silent", "enlist"]) == [["listen", "silent", "enlist"]]

    # 6. 重复的单词
    assert groupAnagram(["rat", "rat"]) == [["rat", "rat"]]

    # 7. 字母相同但长度不同，不算 anagram
    assert groupAnagram(["ab", "ba", "abb"]) == [["ab", "ba"], ["abb"]]

    # 8. 大小写不同，按 ASCII 不算同一组
    assert groupAnagram(["Tar", "rat"]) == [["Tar"], ["rat"]]

    print("test_groupAnagram passed ✅")


def test_merge_vs_quick():
    # 两种算法对同一个输入，结果必须一样
    words = ["rat", "mango", "zyxwvu", "aAbB", "banana", "Hello World", "123abc"]
    for w in words:
        assert mergeSort(list(w)) == quickSort(list(w)), w
    print("test_merge_vs_quick passed ✅")


test_sortString()
test_groupAnagram()
test_merge_vs_quick()