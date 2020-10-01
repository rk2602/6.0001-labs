# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

import math

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    
    answer=[]
    amazon=[]
    alist=[char for char in sequence]
    othlist=[char for char in sequence]
    listminus1=[]
    thechar=''
    if len(alist)==1:
        return alist
    else:
        thechar=alist[0]
        alist.pop(0)
        buh=''.join(alist)
        listminus1=get_permutations(buh)
        for i in range(0,len(listminus1)):
            for j in range(0,len(othlist)):        
                onechar=[char for char in listminus1[i]]
                onechar.insert(j,thechar)
                temp=''.join(onechar)
                answer.append(temp)
                if len(temp)==len(sequence):
                    if temp not in amazon:
                        amazon.append(temp)

        if len(othlist)==len(sequence):
            return amazon
        else:
            return answer
    
if __name__ == '__main__':
#    #EXAMPLE
     example_input = 'abc'
     print('Input:', example_input)
     print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
     print('Actual Output:', get_permutations(example_input))
     
     example_input1 = 'abd'
     print('Input:', example_input1)
     print('Expected Output:', ['abd', 'bad', 'bda', 'adb', 'dab', 'dba'])
     print('Actual Output:', get_permutations(example_input1))
     
     example_input2 = 'abe'
     print('Input:', example_input2)
     print('Expected Output:', ['abe', 'bae', 'bea', 'aeb', 'eab', 'eba'])
     print('Actual Output:', get_permutations(example_input2))

