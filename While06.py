def main(s):
    """
    A variable of type str is given. Find and return how many consonant letters there are.
    Args:
        s: str
        consonant: other than vowels(a, e, i, o, u)
    Returns:
        int: return answer


    """
    vowels="aeiouAEIOU" 
    count =0
    i=0
    while i<len(s):
        if s[i].isalpha():
            count+=1
        i+=1

        return count

s="hello world"
print(main(s))