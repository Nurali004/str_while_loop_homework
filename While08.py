def count_odd_digits(s):
    """
    A string of numbers is given. Find how many odd digits there are and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    count=0
    i=0
    while i<len(s):
        if int(s[i])%2==1:
            count+=1
        i+=1
    return count

s="123456780"
print(count_odd_digits(s))