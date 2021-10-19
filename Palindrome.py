def palindrome(word):
    new_string=""
    reverse_string=""
    for letter in word.strip():
        new_string+=letter.replace(" ","")
        reverse_string=letter.replace(" ","")+reverse_string
    return new_string.lower()==reverse_string.lower()
print(palindrome(input()))