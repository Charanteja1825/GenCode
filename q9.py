def generate_threes(start: int, end: int) -> list[int]:
    if start >= end:
        return []
    return list(range(start, end, 3))

if __name__ == "__main__":
    print(generate_threes(1, 11))
    print(generate_threes(0, 9))
    print(generate_threes(5, 5))
    print(generate_threes(20, 10))
    print(generate_threes(-5, 5))

    assert generate_threes(1, 11) == [1, 4, 7, 10]
    assert generate_threes(0, 9) == [0, 3, 6]
    assert generate_threes(5, 5) == []
    assert generate_threes(20, 10) == []
    assert generate_threes(-5, 5) == [-5, -2, 1, 4]
    print("All test cases passed")
