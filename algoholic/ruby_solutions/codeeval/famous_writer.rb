File.open(ARGV[0]).each_line do |line|
  array = line.split('| ')

  coded_message = array[0]
  numbers = array[1].split(' ')

  numbers.each do | item |
    print coded_message[item.to_i - 1]
  end
  puts
end
