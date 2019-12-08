#!/usr/bin/ruby

# day 2 2019
# intcode program - list of integers seperated by commas.
# opcodes:
#   - 1: adds positions 1 and 2 together and stored in 3rd position
#   - 2: multiples pos 1 and 2 and stores result in pos 3
#   - 99: stop

class Intcode
  attr_accessor :program_list, :pos, :running
  def initialize(in_list)
    @program_list = in_list
    @pos = 0
    @running = true
  end

  def run
    restore_state
    while @running
      do_opcode
    end
  end

  def restore_state
    @program_list[1] = 12
    @program_list[2] = 2
  end

  def do_opcode
    puts "pos #{@pos} doing #{@program_list[@pos]}"
    if @program_list[@pos] == 1
      add
      @pos += 4
    elsif @program_list[@pos] == 2
      mult
      @pos += 4
    elsif @program_list[@pos] == 99
      @running = false
    else
      puts "ERROR! ran into unexpected value #{@program_list[@pos]} at #{@pos}"
      @running = false
    end
  end

  def add
    left_p   = @program_list[@pos + 1]
    right_p  = @program_list[@pos + 2]
    target_p = @program_list[@pos + 3]
    left_v   = @program_list[left_p]
    right_v  = @program_list[right_p]
    target_v = @program_list[target_p]
    puts " add - left_p #{left_p}, right_p #{right_p}, target_p #{target_p}"
    puts "     - left_v #{left_v}, right_v #{right_v}, target_v #{target_v}"
    puts "     - target_p #{target_p} = #{left_v + right_v}"
    @program_list[target_p] = left_v + right_v
  end

  def mult
    left_p   = @program_list[@pos + 1]
    right_p  = @program_list[@pos + 2]
    target_p = @program_list[@pos + 3]
    left_v   = @program_list[left_p]
    right_v  = @program_list[right_p]
    target_v = @program_list[target_p]
    puts " mult - left_p #{left_p}, right_p #{right_p}, target_p #{target_p}"
    puts "      - left_v #{left_v}, right_v #{right_v}, target_v #{target_v}"
    puts "      - target_p #{target_p} = #{left_v * right_v}"
    @program_list[target_p] = left_v * right_v
  end
end


# Open file
# taken from guide https://www.rubyguides.com/2015/05/working-with-files-ruby/#How_to_Read_Files_In_Ruby
file_data = File.read('d02-input.txt').split(',')

intcode = Intcode.new(file_data.map(&:to_i))

intcode.run

puts intcode.program_list.join(',')

puts "The value of pos 0 is #{intcode.program_list[0]}"