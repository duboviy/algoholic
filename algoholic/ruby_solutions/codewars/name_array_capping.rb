# Public: Create a method that capitalize each name in input.
#
# array - Array of names.
#
# Examples
#
#   cap_me(['jo', 'nelson', 'jurie'])
#   # => ['Jo', 'Nelson', 'Jurie']
#
#   cap_me(['KARLY', 'DANIEL', 'KELSEY'])
#   # => ['Karly', 'Daniel', 'Kelsey']
#
# Returns an array.
def cap_me(array)
  array.map(&:capitalize)
end