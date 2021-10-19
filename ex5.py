str_sentence='X-DSPAM-CONFIDENCE:0.8475'
find_one=str_sentence.find(':')
rest_of_string=str_sentence[find_one+1:]
print(float(rest_of_string))