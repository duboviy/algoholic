File.open(ARGV[0]).each_line do |line|
  first = line.split(';')[0]
  second = line.split(';')[1]

  first.split(',').collect { |i| i.to_i }.each do |item|
    print "#{item} " if second.split(',').collect { |i| i.to_i }.include?(item)
  end
  puts
end