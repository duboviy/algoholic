File.open(ARGV[0]).each_line do |line|
  first = line.split('|')[0].split(' ').collect { |i| i.to_i }
  second = line.split('|')[1].split(' ').collect { |i| i.to_i }

  first.each_with_index do |item, index|
    print "#{item * second[index]} "
  end

  puts

end