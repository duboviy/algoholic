# Public: Get the value in the nth index of an arithmetic sequence.
#
# first   - The first value in the 0 INDEX.
# n       - The index of the value we want.
# c       - The constant added between the terms.
#
# Examples
#
#   nthterm(1, 2, 3)
#   # => 7
#
#   nthterm(2, 2, 2)
#   # => 6
#
#   nthterm(-50, 10, 20)
#   # => 150
#
# Returns a number.
def nthterm(first, n, c)
  n.times{ first += c }
  first
end