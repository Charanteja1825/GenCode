def average_passing_grades(grades: list[int]) -> float:
    total = 0
    count = 0
    for g in grades:
        if g >= 50:
            total += g
            count += 1
    return total / count if count else 0.0

if __name__ == "__main__":
    print(average_passing_grades([40, 60, 80, 20]))
    print(average_passing_grades([50, 100]))
    print(average_passing_grades([10, 20, 30]))
    print(average_passing_grades([85]))
    print(average_passing_grades([]))
    
    assert average_passing_grades([40, 60, 80, 20]) == 70.0
    assert average_passing_grades([50, 100]) == 75.0
    assert average_passing_grades([10, 20, 30]) == 0.0
    assert average_passing_grades([85]) == 85.0
    assert average_passing_grades([]) == 0.0

    print("All test cases passed")
