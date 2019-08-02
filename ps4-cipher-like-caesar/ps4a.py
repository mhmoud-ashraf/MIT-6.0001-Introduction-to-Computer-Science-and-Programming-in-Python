# Problem Set 4A
# Name: Mahmoud Ashraf
# Collaborators: None
# Time Spent: -

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

#    pass #delete this line and replace with your code here
    if len(sequence) == 1:
        return [sequence]
    
    else:
        sequence_length = len(sequence)
        first_element = sequence[0]
        sequence = sequence[1::]
        permutation_list = get_permutations(sequence)
        temp_list = permutation_list[:]
        
        for element in temp_list:
            k = 0
            first_element_added = first_element + element
            elements = list(first_element_added)
            
            if first_element_added not in permutation_list:
                permutation_list.append(first_element_added)
            
            for j in range(sequence_length - 1):
                (elements[k],elements[k + 1]) = (elements[k + 1],elements[k])
                k += 1
                perm_temp = ''.join(elements)
                
                if perm_temp not in permutation_list:
                    permutation_list.append(perm_temp)
                    
            permutation_list.remove(element)
                
        return permutation_list



if __name__ == '__main__':
    #EXAMPLE
    example_input = 'abc'
    print('Input:', example_input)
    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    print('Actual Output:', get_permutations(example_input))
    print()
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)

#    pass #delete this line and replace with your code here
    example_input = 'nna'
    print('Input:', example_input)
    print('Expected Output:', ['nna', 'nan', 'ann'])
    print('Actual Output:', get_permutations(example_input))
    print()
    
    example_input = 'aaa'
    print('Input:', example_input)
    print('Expected Output:', ['aaa'])
    print('Actual Output:', get_permutations(example_input))
    print()
    
    example_input = 'hat'
    print('Input:', example_input)
    print('Expected Output:', ['hat', 'aht', 'ath', 'hta', 'tha', 'tah'])
    print('Actual Output:', get_permutations(example_input))
    print()

