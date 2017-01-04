File.open(ARGV[0]).each_line do |line|
  first = line.split(',')[0].to_i
  second = line.split(',')[1].to_i

  while (first / second) >= 1
    first -= second
  end

  puts first
end