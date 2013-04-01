
def is_palindrome_v1(s):
    """
    check whether given string is palindrome or not.
    >>>is_palindrome_v1('dood')
    true
    >>>is_palindrome_v1('hello')
    false
    """
    return reverse(s) == s

def reverse(s):
    """
    reverse a given string
    >>>reverse('dood')
    'dood'
    >>>reverse('hello')
    'olleh'
    >>>reverse('a')
    'a'
    """
    # for each character in string prepend to reverse string
    rev = ''
    for ch in s:
        rev = ch + rev

    return rev


if __name__ == '__main__':
    print is_palindrome_v1('dood')
    print is_palindrome_v1('hello')
