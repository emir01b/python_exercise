def reverse_long_words(sentence):
    words = sentence.split()
    
    for i in range(len(words)):
        if len(words[i]) >= 5:
            words[i] = words[i][::-1]
    
    return ' '.join(words)
sentence = " Tüm bu Siber Güvenlik Uzmanı web sitesi"
print(reverse_long_words(sentence))