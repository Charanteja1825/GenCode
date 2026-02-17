def count_inventory(fruit_list: list[str]) -> dict[str, int]:
    result = {}
    for fruit in fruit_list:
        result[fruit] = result.get(fruit, 0) + 1
    return result

if __name__ == "__main__":
    print(count_inventory(["apple", "banana", "apple", "cherry"]))
    print(count_inventory(["orange", "orange"]))
    print(count_inventory(["grape"]))
    print(count_inventory([]))
    print(count_inventory(["Apple", "apple"]))

    assert count_inventory(["apple", "banana", "apple", "cherry"]) == {"apple": 2, "banana": 1, "cherry": 1}
    assert count_inventory(["orange", "orange"]) == {"orange": 2}
    assert count_inventory(["grape"]) == {"grape": 1}
    assert count_inventory([]) == {}
    assert count_inventory(["Apple", "apple"]) == {"Apple": 1, "apple": 1}

    print("All test cases passed")
