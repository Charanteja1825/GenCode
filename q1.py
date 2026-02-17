def calculate_total_bill(amount: float, tip_percent: int) -> float:
    amount = float(amount)
    tip_percent = float(tip_percent)
    total = amount + (amount * tip_percent / 100)
    return round(total, 2)


if __name__ == "__main__":
    print("Test 1:", calculate_total_bill(100.0, 15))
    print("Test 2:", calculate_total_bill(55.50, 20))
    print("Test 3:", calculate_total_bill(200, 0))
    print("Test 4:", calculate_total_bill(12.99, 10))
    print("Test 5:", calculate_total_bill(0, 15))

    assert calculate_total_bill(100.0, 15) == 115.0
    assert calculate_total_bill(55.50, 20) == 66.6
    assert calculate_total_bill(200, 0) == 200.0
    assert calculate_total_bill(12.99, 10) == 14.29
    assert calculate_total_bill(0, 15) == 0.0

    print("All test cases passed")
