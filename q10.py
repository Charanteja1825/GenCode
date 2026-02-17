def organize_scores(scores: list[int], descending: bool) -> list[int]:
    return sorted(scores, reverse=descending)

if __name__ == "__main__":
    print(organize_scores([10, 5, 8], False))
    print(organize_scores([10, 5, 8], True))
    original = [3, 1, 2]
    print(organize_scores(original, True))
    print(original)
    print(organize_scores([1, 2, 3], False))
    print(organize_scores([], False))

    assert organize_scores([10, 5, 8], False) == [5, 8, 10]
    assert organize_scores([10, 5, 8], True) == [10, 8, 5]
    assert organize_scores(original, True) == [3, 2, 1]
    assert original == [3, 1, 2]
    assert organize_scores([1, 2, 3], False) == [1, 2, 3]
    assert organize_scores([], False) == []

    print("All test cases passed")
