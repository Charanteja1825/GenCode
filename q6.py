def convert_temperature(value: float, unit: str):
    if unit == 'C':
        return round((value * 9/5) + 32, 1)
    if unit == 'F':
        return round((value - 32) * 5/9, 1)
    return "Invalid Unit"

if __name__ == "__main__":
    print(convert_temperature(0, 'C'))
    print(convert_temperature(100, 'F'))
    print(convert_temperature(100, 'C'))
    print(convert_temperature(-40, 'F'))
    print(convert_temperature(25, 'K'))

    assert convert_temperature(0, 'C') == 32.0
    assert convert_temperature(100, 'F') == 37.8
    assert convert_temperature(100, 'C') == 212.0
    assert convert_temperature(-40, 'F') == -40.0
    assert convert_temperature(25, 'K') == "Invalid Unit"

    print("All test cases passed")
