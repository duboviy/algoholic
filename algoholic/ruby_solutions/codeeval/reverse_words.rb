File.open(ARGV[0]).each_line do |line|
  array = line.split(' ')

  result = ''

  array.reverse.each do |item|
    result += item + ' '
  end

  puts result.strip
end