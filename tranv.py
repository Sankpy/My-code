def tranv_str(sentence):
    count=0
    lenth_of_the_string=len(sentence)
    while count<lenth_of_the_string:
          part_sentence=sentence[lenth_of_the_string-1]
          print(part_sentence)
          lenth_of_the_string-=1
tranv_str('I reside on the bank of the river Ganges')          