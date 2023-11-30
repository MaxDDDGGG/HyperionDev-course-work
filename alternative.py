# Input that chnages all text to lowercase
string_letters = input("Please enter text: ").lower() 

# Non-letter checker
while any (not chr.isalpha() and chr!=' ' for chr in string_letters):
    print("Only enter letters!")
    string_letters = input("Please enter text: ")
else:
# Create lowercase and uppercase strings
    lowercase = string_letters.lower()
    uppercase = string_letters.upper()

# zip together the 2 string
    wibbly_wobbly = ''.join([a + b for a, b in zip(lowercase[::2], uppercase[1::2])])

# Include the last letter if the length is odd
    if len(string_letters) % 2 != 0:
        wibbly_wobbly += string_letters[-1]

    print(wibbly_wobbly)

# Input that chnages all text to uppercase
string_words = input("Enter some words: ").upper()

# print (string_words) - This was a check statement

# Non-letter checker
while any(not chr.isalpha() and chr != ' ' for chr in string_words):
    print("Only enter letters and spaces!")
    string_words = input("Please enter text: ")

# Split the string_words in to a list of words
words_list = string_words.split()

# The 2 lists prepared for uppercase and lowercase words
uppercased_words = []
lowercased_words = []

# Select every second word to be uppercase, every other word to be made lowercase
for i in range(len(words_list)):
    if i % 2 == 0:
        uppercased_words.append(words_list[i].upper())
    else:
        lowercased_words.append(words_list[i].lower())

# Join the two strings of uppercase and lowercase words together to make a caterpillar
word_caterpillar = ' '.join([a + ' ' + b for a, b in zip(uppercased_words, lowercased_words)])

# Additional part to include the last word, for an odd number of words
# Is there a better way of doing this?
if len(words_list) % 2 != 0:
    word_caterpillar += ' ' + words_list [-1]
print(word_caterpillar)