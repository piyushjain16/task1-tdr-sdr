# Problem Set 4A


def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    #>>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    ['bc','cb']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    if len(sequence)==1:
        return [sequence]
    else:
        l=get_permutations(sequence[1:])
        per=[]
        for i in l:
            for x in range(len(i)+1):
                s=''
                added=False
                for y in range(len(i)+1):
                    if y==len(i) and not added:
                        s+=sequence[0]
                    elif y==len(i):
                        pass
                    elif x==y:
                        s+=sequence[0]+i[y]
                        added=True
                    else:
                        s+=i[y]
                per.append(s)
        return per

if __name__ == '__main__':
    s=input("Enter the string:")
    print("all the possible permutation are",get_permutations(s))
#   #EXAMPLE
#   example_input = 'abc'
#   print('Input:', example_input)
#   print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
#   print('Actual Output:', get_permutations(example_input)) 
#   # Put three example test cases here (for your sanity, limit your inputs
#   to be three characters or fewer as you will have n! permutations for a 
#   sequence of length n)




