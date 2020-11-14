def spin_words(sentence):
    split = sentence.split(' ')
    for i, word in enumerate(split):
      if len(word) > 4:
        split[i] = word[::-1]

    return ' '.join(split)



print(spin_words('Welcome'))
# returns emocleW
print(spin_words('Hey fellow warriors'))
# returns Hey wollef sroirraw
print(spin_words('This is a test'))
# returns 'This is a test'
print(spin_words('This is another test'))
# returns 'This is rehtona test'


