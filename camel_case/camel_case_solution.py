def to_camel_case(text):
  dash = text.find('-')
  underscore = text.find('_')

  if dash == -1 and underscore == -1:
    return text
  elif dash > -1:
    new_text = text.replace('-' + text[dash + 1], f'{text[dash + 1]}'.upper(), 1)
    return to_camel_case(new_text)
  elif underscore > -1:
    new_text = text.replace('_' + text[underscore + 1], f'{text[underscore + 1]}'.upper(), 1)
    return to_camel_case(new_text)


print(to_camel_case("the-stealth-warrior"))
# returns "theStealthWarrior"
print(to_camel_case("The_Stealth_Warrior"))
# returns "TheStealthWarrior"
