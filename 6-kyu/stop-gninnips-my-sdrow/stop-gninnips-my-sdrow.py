def spin_words(sentence):
    reverse_word = ""
    index_count = 0
    # split sentence into words
    words = sentence.split()
    # for each word, determine if it is three letters long or less. if so, leave it and move onto the next word
    for word in words:
     # if yes, make new list, [::-1], replace method back into place, set list to ""
        list_word = list(word)
        if len(word) >= 5:
            reverse_word = list_word[::-1]
            final_reverse_word = "".join(reverse_word)
            words[index_count] = final_reverse_word
            index_count = index_count + 1
        elif len(word) < 5:
            reverse_word = list_word
            final_reverse_word = "".join(reverse_word)
            words[index_count] = final_reverse_word
            index_count = index_count + 1
​
    return " ".join(words)
​
​
​