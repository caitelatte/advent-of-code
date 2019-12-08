#!/usr/bin/ruby

# find the total fuel requirements given a list of modules' mass
# fuel_for_module = (mass / 3).roundeddown - 2

# Open file
# taken from guide https://www.rubyguides.com/2015/05/working-with-files-ruby/#How_to_Read_Files_In_Ruby
file = File.open('d01-input.txt')
file_data = file.readlines.map(&:chomp)
file.close

def calc_fuel_cost(mass)
  # lesson: pay attention to spaces and implicit argument passing!
  # wrong number of arguments (given 1, expected 0) (ArgumentError)
  # (mass.to_f / 3).to_i -2 
  (mass.to_f / 3).to_i - 2
end

def calc_fuel_cost_recursively(mass)
  additional_fuel = calc_fuel_cost(mass)
  puts "#{mass} requires #{additional_fuel}. calc recursively:"
  module_total_fuel = 0
  while additional_fuel.positive?
    module_total_fuel += additional_fuel
    additional_fuel = calc_fuel_cost(additional_fuel)
    puts "  additional_fuel requires #{additional_fuel} extra"
  end
  puts "  #{mass} requires in total #{module_total_fuel}"
  module_total_fuel
end

total_fuel_required = 0

file_data.each { |file_line|
  # total_fuel_required += (file_line.to_f / 3).to_i - 2
  total_fuel_required += calc_fuel_cost(file_line)
}

puts 'total fuel: ' + total_fuel_required.to_s

# Part 2: need to recursively calculate fuel cost of fuel as well!

part2_total_fuel_required = 0

file_data.each { |file_line| part2_total_fuel_required += calc_fuel_cost_recursively(file_line) }

puts 'phase 2 total fuel: ' + part2_total_fuel_required.to_s
