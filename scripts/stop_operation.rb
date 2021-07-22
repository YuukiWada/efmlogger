#!/usr/bin/env ruby
require "pi_piper"
require "time"

day = Date.today
pin=PiPiper::Pin.new(:pin => 20, :direction => :in)

time=Time.now
time_past=time.strftime("%Y%m%d")

loop do
  time=Time.now
  time_now=time.strftime("%Y%m%d")
  pin.read
  if pin.off? then
    process=`pgrep -f read_mcp`
    if process != "" then
      `pkill -f read_mcp`
    end
  elsif time_now!=time_past then
    process=`pgrep -f read_mcp`
    if process != "" then
      `pkill -f read_mcp`
    end
  end
  sleep(5.0)
end
