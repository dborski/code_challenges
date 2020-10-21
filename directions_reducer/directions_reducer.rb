OPPOSITES = {
  "NORTH": "SOUTH",
  "EAST": "WEST"
}

def dirReduc(arr)
  arr_length = arr.length
  
  holder = ''
  arr.each_with_index do |direction, index|
    if index > 0 && (OPPOSITES[holder.to_sym] == direction || OPPOSITES.key(holder) == direction.to_sym)
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