File.open(ARGV[0]).each_line do |line|
  line.split(',').collect { |item| item.to_i }.uniq.each { |item| print "#{item} "}
  puts
end