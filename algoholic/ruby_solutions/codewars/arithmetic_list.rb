# Public: Create arithmetic list which is basically a list that contains consecutive terms in the sequence.
#
# first - The first term in the sequence.
# c     - The constant that you are going to add.
# l     - The number of terms that should be returned.
#
# Examples
#
#   seqlist(0,1,20)
#   # => [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
#
# Returns an array.
def seqlist(first, c, l)
  arr = [first]
  (l - 1).times { arr << (first += c) }; arr
end