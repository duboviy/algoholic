# Public: To convert strings to how they would be written by Jaden Smith (always capitalizing every word).
#
# Examples
#
#   "How can mirrors be real if our eyes aren't real".toJadenCase
#   # => "How Can Mirrors Be Real If Our Eyes Aren't Real"
#
# Returns the modified string.
class String
  def toJadenCase
    self.split.map(&:capitalize).join(' ')
  end
end