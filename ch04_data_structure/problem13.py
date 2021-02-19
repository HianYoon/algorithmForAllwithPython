# 13-1
def is_palindrome(st):
    if not isinstance(st, str):
        print("The input is not an instance of Type: str")
        return False

    # change every character to lower case
    st = st.lower()

    char_list = list(st)
    length = len(char_list)
    for i in range(0, length):
        i = length - 1 - i  # the index starts from the last index due to 'out of bound exception'
        if not char_list[i].isalpha():
            char_list.pop(i)
    
    return palindrome_test(char_list, 0, len(char_list) - 1)


def palindrome_test(li, left, right):
    # terminating condition
    if left > right:
        return True

    if li[left] != li[right]:
        return False
    else:
        left += 1
        right -= 1
        return palindrome_test(li, left, right)


s = "power"
print(s, is_palindrome(s))
s = "toot"
print(s, is_palindrome(s))
s = "Wow"
print(s, is_palindrome(s))
s = "Madam, I'm Adam."
print(s, is_palindrome(s))
