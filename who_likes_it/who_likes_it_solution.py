def likes(names):
  payload = ''

  if len(names) == 0:
    payload = 'no one likes this'
  elif len(names) == 1:
    payload = f'{names[0]} likes this'
  elif len(names) == 2:
    payload = ' and '.join(names) + ' like this'
  elif len(names) == 3:
    payload = names[0] + ', ' + names[1] +  ' and ' + names[2] + ' like this'
  else:
    payload = names[0] + ', ' + names[1] + ' and ' + f'{len(names) - 2} others like this'

  return payload


print(likes([]))
# returns "no one likes this"
print(likes(["Peter"]))
# returns "Peter likes this"
print(likes(["Jacob", "Alex"]))
# returns "Jacob and Alex like this"
print(likes(["Max", "John", "Mark"]))
# returns "Max, John and Mark like this"
print(likes(["Alex", "Jacob", "Mark", "Max"]))
# returns "Alex, Jacob and 2 others like this"