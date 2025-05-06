def main(s):
    """
    A string of numbers is given. Find the sum of all the digits and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    yigindi=0
    i=0
    while i<len(s):
        if s[i].isdigit():
            yigindi+=int(s[i])

        i+=1
    return yigindi

s="1234fhjfjf"
print(main(s))