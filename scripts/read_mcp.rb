#!/usr/bin/env ruby
require "pi_piper"

start=Time.now.strftime('%s%L').to_i
puts "#{(start/1000.0).round(3)}"

PiPiper::Spi.begin do |spi|
  loop do
    first, center, last = spi.write [0b00000001, 0b10000000, 0b00000000]
    center = center & 0b00001111
    center = center << 8
    adc =  center + last

    first, center, last = spi.write [0b00000001, 0b11000000, 0b00000000]
    center = center & 0b00001111
    center = center << 8
    pps =  center + last

    puts "#{((Time.now.strftime('%s%L').to_i-start)/1000.0).round(3)},#{adc},#{pps}"
    sleep 0.035
    
  end
end
