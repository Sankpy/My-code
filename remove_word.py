def replace_ending(sentence,old,new):
    new_sentence=''
    if sentence.endswith(old)==True:
        sentence_list=sentence.split()
        Part_of_sentence=sentence_list[:-1]
        Part_of_sentence.append(new)
        for words in Part_of_sentence:
            new_sentence+=words+" "
        return new_sentence
    return sentence
print(replace_ending("It's raining cats and cats", "cats", "dogs"))
# Should display "It's raining cats and dogs"
print(replace_ending("She sells seashells by the seashore", "seashells", "donuts")) 
# Should display "She sells seashells by the seashore"
print(replace_ending("The weather is nice in May", "may", "april")) 
# Should display "The weather is nice in May"
print(replace_ending("The weather is nice in May", "May", "April")) 
# Should display "The weather is nice in April"