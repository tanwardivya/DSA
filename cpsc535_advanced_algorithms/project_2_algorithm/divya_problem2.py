from typing import List
def longest_chain(words: List[str]) -> List[str]:
    """Longest string chain from given list of words

    Args:
        words (List[str]): Array of words

    Returns:
        (List[str]): Array of word in chain
    """
    dp = {}
    # Sort the array of words in ascending order
    sorted_words = sorted(words, key=len)
    for w in sorted_words:
        dp[w] = {}
        dp[w]['chain'] = [] # Store the chain for a word
        dp[w]['length_so_far'] = 0 # Store the maximum length of word in a chain
        for i in range(len(w)):
            prev = w[:i]  + w[i + 1:] # Create a string by removing a single character
            # Check length of string greater then 1 and check
            #if we already previously found the string in calculated solution so far
            # Since we are interested in one of longest chain, to fulfil the criteria don't add if length of string is same or less then length so far in the chain
            if len(prev) > 1 and prev in dp and len(prev) > dp[w]['length_so_far']:
                dp[w]['chain'].extend(dp[prev]['chain']) # Update chain of current word by addng chain of prev word
                dp[w]['chain'].append(prev) # Add the prev word in chain
                dp[w]['length_so_far'] = max(len(prev), dp[w]['length_so_far']) # Update the length so far

    final_result= dp[sorted_words[-1]]['chain']
    # Returns an empty list
    if len(final_result) == 0:
        return []
    #append the longest words to final result
    final_result.append(sorted_words[-1])
    #Returns final sorted list in descending order
    return sorted(final_result, key=len, reverse=True)



if __name__ == '__main__':
    sample =  ["abde", "abc", "abd", "abcde", "ade", "ae", "1abde", "abcdef"]
    result = longest_chain(sample)
    print(f'Longest Chain:{result}')
    print(result)
    sample = ["bdca"]
    result = longest_chain(sample)
    print(f'Longest Chain:{result}')