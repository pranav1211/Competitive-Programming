def score_words(words):
    vowels = 'aeiouy'
    score = 0    
    for single_word in words:  # Iterate over each word in the list        
        vowelcount = 0
        for char in single_word:  # Count vowels in the current word            
            if char in vowels:
                vowelcount += 1
        if vowelcount % 2 == 0:
            score += 2       
        else:
            score += 1
    return score