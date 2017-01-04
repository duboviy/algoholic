def morse_code(array)
  result_string = ''
  # puts array.inspect
  a = '.-'
  b = '-...'
  c = '-.-.'
  d = '-..'
  e = '.'
  f = '..-.'
  g = '--.'
  h = '....'
  i = '..'
  j = '.---'
  k = '-.-'
  l = '.-..'
  m = '--'
  n = '-.'
  o = '---'
  p = '.--.'
  q = '--.-'
  r = '.-.'
  s = '...'
  t = '-'
  u = '..-'
  v = '...-'
  w = '.--'
  x = '-..-'
  y = '-.--'
  z = '--..'

  n1 = '.----'
  n2 = '..---'
  n3 = '...--'
  n4 = '....-'
  n5 = '.....'
  n6 = '-....'
  n7 = '--...'
  n8 = '---..'
  n9 = '----.'
  n0 = '-----'

  array.each do |item|
    case item
      when a then result_string += 'A'
      when b then result_string += 'B'
      when c then result_string += 'C'
      when d then result_string += 'D'
      when e then result_string += 'E'
      when f then result_string += 'F'
      when g then result_string += 'G'
      when h then result_string += 'H'
      when i then result_string += 'I'
      when j then result_string += 'J'
      when k then result_string += 'K'
      when l then result_string += 'L'
      when m then result_string += 'M'
      when n then result_string += 'N'
      when o then result_string += 'O'
      when p then result_string += 'P'
      when q then result_string += 'Q'
      when r then result_string += 'R'
      when s then result_string += 'S'
      when t then result_string += 'T'
      when u then result_string += 'U'
      when v then result_string += 'V'
      when w then result_string += 'W'
      when x then result_string += 'X'
      when y then result_string += 'Y'
      when z then result_string += 'Z'

      when n1 then result_string += '1'
      when n2 then result_string += '2'
      when n3 then result_string += '3'
      when n4 then result_string += '4'
      when n5 then result_string += '5'
      when n6 then result_string += '6'
      when n7 then result_string += '7'
      when n8 then result_string += '8'
      when n9 then result_string += '9'
      when n0 then result_string += '0'
    end
  end
  result_string
end

File.open(ARGV[0]).each_line do |line|

  line.split('  ').each do |sub|
     print "#{morse_code(sub.split(' '))} "
  end

  puts
end
