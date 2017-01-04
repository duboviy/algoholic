# Public: Create function to count score in dart game.
#
# radiuses - An array of radiuses (can be integers and/or floats).
#
# Scoring specifications:
# 0 points - radius above 10
# 5 points - radius between 5 and 10 inclusive
# 10 points - radius less than 5
#
# Examples
#
#   scoreThrows([1, 5, 11])
#   # => 15
#
#   scoreThrows([15, 20, 30])
#   # => 0
#
#   scoreThrows([1, 2, 3, 4])
#   # => 140
#
# Returns total number score.
def scoreThrows(radiuses)
  result = radiuses.inject(0) { |sum, i| (0...5).include?(i) ? sum += 10 : (5..10).include?(i) ? sum += 5 : sum += 0 }
  ((result == radiuses.size*10) and not radiuses.empty?) ? result += 100 : result
end
