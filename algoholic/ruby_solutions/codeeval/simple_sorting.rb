File.open(ARGV[0]).each_line do |line|

  line.split(' ').collect { |i| i.to_f }.sort.each do |item|
    print  "%.3f " % item
  end
  puts
end