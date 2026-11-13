import re
 
 
def validate_email(email: str) -> bool:
    """Проверяет корректность email."""
    pattern = r"^[\w.+-]+@[\w-]+\.[\w.-]+$"
    return bool(re.match(pattern, email))
 
 
def validate_phone(phone: str) -> bool:
    """Проверяет корректность российского телефона."""
    pattern = r"^\+7[\s-]?\(?\d{3}\)?[\s-]?\d{3}[\s-]?\d{2}[\s-]?\d{2}$"
    return bool(re.match(pattern, phone))
 
 
def validate_url(url: str) -> bool:
    """Проверяет корректность URL."""
    pattern = r"^https?://[\w.-]+\.[a-z]{2,}(/[\w./-]*)?$"
    return bool(re.match(pattern, url))
 
 
tests = [
    ("email", "ivan@example.com", validate_email),
    ("email", "invalid@", validate_email),
    ("email", "no-at-sign.com", validate_email),
    ("phone", "+7 (999) 123-45-67", validate_phone),
    ("phone", "+79991234567", validate_phone),
    ("phone", "8-999-123", validate_phone),
    ("url", "https://example.com", validate_url),
    ("url", "http://site.ru/path/page", validate_url),
    ("url", "not-a-url", validate_url),
]
 
for type_, value, validator in tests:
    result = "✓" if validator(value) else "✗"
    print(f"{result} {type_}: {value}")