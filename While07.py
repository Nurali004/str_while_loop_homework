def main(s):
    """
    A string of numbers is given. Find how many even digits there are and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    count=0
    i=0
    while i<len(s):
        if s[i].isdigit():
            count+=1
        i+=1

    return count
s="fehjerghhg1234"
print(main(s))
