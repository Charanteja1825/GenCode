def sanitize_email(raw_input: str) -> str:
    cleaned = raw_input.strip().lower()
    if cleaned.count('@') == 1:
        return cleaned
    return "Invalid Email"

if __name__ == "__main__":
    print(sanitize_email("  User@Example.com  "))
    print(sanitize_email("test@domain.org"))
    print(sanitize_email("myname.website.com"))
    print(sanitize_email("admin@@company.com"))
    print(sanitize_email("   "))

    assert sanitize_email("  User@Example.com  ") == "user@example.com"
    assert sanitize_email("test@domain.org") == "test@domain.org"
    assert sanitize_email("myname.website.com") == "Invalid Email"
    assert sanitize_email("admin@@company.com") == "Invalid Email"
    assert sanitize_email("   ") == "Invalid Email"

    print("All test cases passed")
