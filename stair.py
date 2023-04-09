def find_missing_words(s, t):
    # split strings into lists of words
    s_words = s.split()
    t_words = t.split()
    
    # initialize list of missing words
    missing_words = []
    
    # iterate through words in s, adding missing words to the list
    for word in s_words:
        if word not in t_words:
            missing_words.append(word)
    
    return missing_words

s = "The quick brown fox jumps over the lazy dog"
t = "The brown jumps the dog"

missing_words = find_missing_words(s, t)
print(missing_words)
