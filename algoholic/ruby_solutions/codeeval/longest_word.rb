File.open(ARGV[0]).each_line do |line|

  array = line.split(' ')
  puts array.inspect

  longest = array[0]
  array.each do |element|
    puts "#{element.length}"
    if longest.length < element.length
      longest = element
    else
      next
    end
  end
  puts '======'
  puts "LONGEST = #{longest} with lengths #{longest.length}"
  puts '======'
end
