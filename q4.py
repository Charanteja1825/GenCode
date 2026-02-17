def get_ticket_price(age: int, is_student: bool) -> int:
    if age < 12:
        return 8
    if age >= 65:
        return 10
    return 12 if is_student else 15

if __name__ == "__main__":
    print(get_ticket_price(10, False))
    print(get_ticket_price(70, True))
    print(get_ticket_price(20, True))
    print(get_ticket_price(25, False))
    print(get_ticket_price(12, False))
    
    assert get_ticket_price(10, False) == 8
    assert get_ticket_price(70, True) == 10
    assert get_ticket_price(20, True) == 12
    assert get_ticket_price(25, False) == 15
    assert get_ticket_price(12, False) == 15

    print("All test cases passed")

