def count(sentence):
    sentence_list=sentence.split()
    count_words=0
    count_letters=0
    for words in sentence_list:
        count_words+=1
        for letters in words:
            count_letters+=1
    return ("sentence:{},words:{},Letters:{}".format(sentence,count_words,count_letters))
print(count('Kolkata is city of joy'))    