# Public: Create a list of the individual digits in order.
#
# n   - Non-negative integer.
#
# Examples
#
#   digitize(123)
#   # => [1, 2, 3]
#
#   digitize(1)
#   # => [1]
#
#   digitize(8675309)
#   # => [8,6,7,5,3,0,9]
#
# Returns an array.
def digitize(n)
  n.to_s.chars.map(&:to_i)
end