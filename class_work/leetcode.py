def isValid(s):
    pairs = {
        "):("
        "]:["
        "}:{"
    }
    stack = [
        
    ]
    for character in s:
        if character in pairs:
            if stack and stack[-1] == pairs[character]:
                stack.pop()
            else:
                return False
        else:
            stack.append(character)
    if stack:
        return False
    else:
        return True

test_string_1 = "(){}([{{}}])"
test_string_2 = "({[]})"
test_string_3 = "(){])"
test_string_4 = "({{}}])"

print(isValid(test_string_1))
print(isValid(test_string_2))
print(isValid(test_string_3))
print(isValid(test_string_4))