def dirReduc(arr)
  opposites = {
    "NORTH": "SOUTH",
    "EAST": "WEST"
  }
  arr_length = arr.length
  
  holder = ''
  arr.each_with_index do |direction, index|
    if index > 0 && (opposites[holder.to_sym] == direction || opposites.key(holder) == direction.to_sym)
      arr.slice!(index - 1, 2)
      holder = ''
    else
      holder = direction
    end 
  end
  dirReduc(arr) if arr.length < arr_length
  return arr
end

a = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
u = ["NORTH", "WEST", "SOUTH", "EAST"]

p dirReduc(a)
p dirReduc(u)