def convert_seconds(total_seconds: int) -> str:
    minutes = total_seconds // 60
    seconds = total_seconds % 60
    return f"{minutes}m {seconds}s"

if __name__ == "__main__":
    print(convert_seconds(125))
    print(convert_seconds(60))
    print(convert_seconds(45))
    print(convert_seconds(3600))
    print(convert_seconds(0))
    
    assert convert_seconds(125) == "2m 5s"
    assert convert_seconds(60) == "1m 0s"
    assert convert_seconds(45) == "0m 45s"
    assert convert_seconds(3600) == "60m 0s"
    assert convert_seconds(0) == "0m 0s"

    print("All test cases passed")
