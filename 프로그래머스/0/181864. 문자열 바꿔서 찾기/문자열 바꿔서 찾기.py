def solution(myString, pat):
    changed = ""
    for ch in myString:
        if ch == "A":
            changed += "B"
        else:
            changed += "A"

    return 1 if pat in changed else 0
