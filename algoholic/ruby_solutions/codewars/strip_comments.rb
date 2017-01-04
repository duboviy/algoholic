# Public: Complete the solution so that it strips all text that follows any of a set of comment markers passed in.
#
# input   - Initial string.
# markers - Array of markers to strip off text after them.
#
# Examples
#
#   solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])
#   # => "apples, pears\ngrapes\nbananas"
#
# Returns modified string.
def solution(input, markers)
  input.gsub(/.[#{markers.inject(:+)}](.*?\\n|.*)/, '')
end