
def is_palindrome_v2(s):
    """ (str) -> (bool)
    Return true if and only if s is palindrome
    >>>is_palindrome_v1('dood')
    true
    >>>is_palindrome_v1('hello')
    false
    """
    # The number of chars in s
    n = len(s)

    # Compare the first half of s to the reverse of the second half of the s.
    return s[:n] == reverse(s[n - n // 2:]) 

def reverse(s):
    """ (str) -> (str)
    Return a reversed version of s
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
