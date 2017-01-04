=begin
'PENNY': .01,
'NICKEL': .05,
'DIME': .10,
'QUARTER': .25,
'HALF DOLLAR': .50,
'ONE': 1.00,
'TWO': 2.00,
'FIVE': 5.00,
'TEN': 10.00,
'TWENTY': 20.00,
'FIFTY': 50.00,
'ONE HUNDRED': 100.00
=end

module Money

  PENNY       = 0.01
  NICKEL      = 0.05
  DIME        = 0.10
  QUARTER     = 0.25
  HALF_DOLLAR = 0.50
  ONE         = 1.00
  TWO         = 2.00
  FIVE        = 5.00
  TEN         = 10.00
  TWENTY      = 20.00
  FIFTY       = 50.00
  ONE_HUNDRED = 100.00

end

File.open(ARGV[0]).each_line do |line|
  # purchase price
  pp = line.split(';')[0].to_f

  # cash given
  ch = line.split(';')[1].to_f

  if ch < pp
    puts 'ERROR'
  elsif ch == pp
    puts 'ZERO'
  else
    change = ch - pp

    # string to output
    str = ''

    # contains constants
    include Money

    while change / ONE_HUNDRED >= 1
      str += 'ONE HUNDRED,'
      change -= ONE_HUNDRED
    end

    while change / FIFTY >= 1
      str += 'FIFTY,'
      change -= FIFTY
    end
    while change / TWENTY >= 1
      str += 'TWENTY,'
      change -= TWENTY
    end
    while change / TEN >= 1
      str += 'TEN,'
      change -= TEN
    end

    while change / FIVE >= 1
      str += 'FIVE,'
      change -= FIVE
    end

    while change / TWO >= 1
      str += 'TWO,'
      change -= TWO
    end

    while change / ONE >= 1
      str += 'ONE,'
      change -= ONE
    end

    while change / HALF_DOLLAR >= 1
      str += 'HALF DOLLAR,'
      change -= HALF_DOLLAR
    end

    while change / QUARTER >= 1
      str += 'QUARTER,'
      change -= QUARTER
    end

    while change / DIME >= 1
      str += 'DIME,'
      change -= DIME
    end

    while change / NICKEL >= 1
      str += 'NICKEL,'
      change -= NICKEL
    end

    while change / PENNY > 0
      str += 'PENNY,'
      change -= PENNY
    end

    puts str.chomp(',')
  end
end