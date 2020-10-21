require 'pry'

def persistence(n, counter = 0)
  # multiply all digits in n together, and then save the answer in a variable
  # with a recursive solution, we will then keep multiplying the numbers until 
  if n < 10
    return counter
  else
    counter += 1
    n = n.digits.reduce(:*)
    persistence(n, counter)
  end 
end

p persistence(39)
p persistence(4)
p persistence(25)
p persistence(999)