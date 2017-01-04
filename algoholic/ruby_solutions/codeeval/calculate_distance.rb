File.open(ARGV[0]).each_line do |line|
  array = line.scan(/-?\d+/)
  x1, y1, x2, y2 = array[0].to_i, array[1].to_i, array[2].to_i, array[3].to_i

  first, second = (x2-x1)**2, (y2-y1)**2

  puts Math.sqrt(first + second).to_i
end
