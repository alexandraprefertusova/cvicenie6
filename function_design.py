# function_design.py

def analyze_password(password,
                     min_length=8,
                     require_digit=True,
                     require_upper=True,
                     require_symbol=False,
                     banned_words=None):

    if banned_words is None:
        banned_words = ['heslo', 'password', '1234']

    symbols = "!@#$%^&*()-_=+[]{};:,.?"
    missing = []

    rules = {
        "min_length": len(password) >= min_length,
        "digit": (not require_digit) or any(c.isdigit() for c in password),
        "upper": (not require_upper) or any(c.isupper() for c in password),
        "symbol": (not require_symbol) or any(c in symbols for c in password),
        "banned_word": not any(w.lower() in password.lower() for w in banned_words)
    }


    for rule, ok in rules.items():
        if not ok and (rule != "symbol" or require_symbol) \
                  and (rule != "digit" or require_digit) \
                  and (rule != "upper" or require_upper):
            missing.append(rule)

    active_rules = 2 + require_digit + require_upper + require_symbol
    passed = active_rules - len(missing)

    score = int(passed / active_rules * 100)
    strong = passed == active_rules

    return strong, score, missing


# TESTY
print(analyze_password("Abc12345!", 8, True, True, True))
print("Pozičné argumenty sú krátke, ale nie je hneď jasné čo ktorá hodnota znamená.")

print()

print(analyze_password("Abc12345!", 8, require_symbol=True))
print("Mix zlepšuje čitateľnosť – menej jasné parametre sú pomenované.")

print()

print(analyze_password("Abc12345", require_symbol=False))
print("Pomenovaný argument jasne ukazuje, že symbol nie je požadovaný.")

print()

print(analyze_password("Admin123!", banned_words=["admin", "root", "test"]))
print("Funkciu možno jednoducho prispôsobiť vlastným zoznamom zakázaných slov.")