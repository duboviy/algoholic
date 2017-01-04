# Public: To implement simple calculator which uses fluent syntax.
#
# Examples
#
#   Calc.new.one.plus.two
#   # => 3
#
#   Calc.new.five.minus.six
#   # => -1
#
#   Calc.new.seven.times.two
#   # => 14
#
#   Calc.new.nine.divided_by.three
#   # => 3
#
# Returns a number.
class Calc
  @state = nil
  @result = 0

  def one
    @state.nil? ? @result = 1 : eval("return #{@result} #{@state} 1")
    self
  end
  def two
    @state.nil? ? @result = 2 : eval("return #{@result} #{@state} 2")
    self
  end

  def three
    @state.nil? ? @result = 3 : eval("return #{@result} #{@state} 3")
    self
  end
  def four
    @state.nil? ? @result = 4 : eval("return #{@result} #{@state} 4")
    self
  end
  def five
    @state.nil? ? @result = 5 : eval("return #{@result} #{@state} 5")
    self
  end
  def six
    @state.nil? ? @result = 6 : eval("return #{@result} #{@state} 6")
    self
  end
  def seven
    @state.nil? ? @result = 7 : eval("return #{@result} #{@state} 7")
    self
  end
  def eight
    @state.nil? ? @result = 8 : eval("return #{@result} #{@state} 8")
    self
  end
  def nine
    @state.nil? ? @result = 9 : eval("return #{@result} #{@state} 9")
    self
  end
  def ten
    @state.nil? ? @result = 10 : eval("return #{@result} #{@state} 10")
    self
  end

  def plus
    @state = '+'
    self
  end

  def minus
    @state = '-'
    self
  end

  def times
    @state = '*'
    self
  end

  def divided_by
    @state = '/'
    self
  end
end