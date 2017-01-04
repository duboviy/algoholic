input_file = File.new("#{ARGV[0]}", 'r')

def print_result(input)
  while (line = input.gets)
    line.each_char do |char|
      if char == char.downcase
        print char.upcase
      elsif char == char.upcase
        print char.downcase
      end
    end
  end
end

print_result(input_file)