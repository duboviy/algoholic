# Public: Get the recursive sum of all the digits in a number.
#
# n   - Natural number.
#
# Examples
#
#   digital_root(16)
#   # => 7
#
#   digital_root(942)
#   # => 6
#
# Returns an array.
def digital_root(n)
  n > 9 ? digital_root(n.to_s.chars.map(&:to_i).inject(:+)) : n
end