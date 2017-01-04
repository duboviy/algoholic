File.open(ARGV[0]).each_line do |line|
  sum = 0
  line.split('').each { |item| sum += item.to_i}
  puts sum
end