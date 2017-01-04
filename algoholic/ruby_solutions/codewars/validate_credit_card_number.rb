# Public: To implement The Luhn Algorithm, which is used to help validate credit card numbers.
#
# n   - Positive integer of up to 16 digits.
#
# Examples
#
#   validate(891)
#   # => false
#
#   validate(1714)
#   # => false
#
#   validate(4532049659615906)
#   # => true
#
# Returns a bool.
def validate(n)
  arr = n.to_s.chars.map(&:to_i)
  arr.size.even? ? arr.each_with_index { |i, index| arr[index] = i * 2 if (index % 2) == 0 } :
      arr.each_with_index { |i, index| arr[index] = i * 2 if (index % 2) == 1 }
  arr.map! { |i| i > 9 ? i.to_s.chars.map(&:to_i).inject(:+) : i }
  (arr.inject(:+) % 10) == 0
end