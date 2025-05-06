def count_uppercase(s):
    """
    A variable of type str is given. Find how many uppercase letters there are and return.
    Args:
        s: str
    Returns:
        int: return answer

    """
    count=0
    i=0
    while i<len(s):
        if s[i].isupper():
            count+=1
        i+=1
    return count

s="Hello Teacher"
print(count_uppercase(s))