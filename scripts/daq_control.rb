#!/usr/bin/env ruby
require "pi_piper"
require "time"

input_dir="/media/pi/data"


def check_usb(input_dir)
  device_path="/dev/sda1"
  
  if !File.exist?(input_dir) then
    `sudo mkdir -p #{input_dir}`
  end
  loop do
    if File.exist?(device_path) then
      result=`mountpoint #{input_dir}`
      if result.chomp=="#{input_dir} is not a mountpoint" then
        puts "/dev/sda1 is not mounted."
        `sudo umount #{device_path}`
        sleep(2.0)
        `sudo mount #{device_path} #{input_dir}`
        sleep(2.0)
      end
      
      result=`mountpoint #{input_dir}`
      if result.chomp!="#{input_dir} is not a mountpoint" then
        puts "/dev/sda1 is mounted."
        return 0
      end
    else
      puts "/dev/sda1 is not inserted."
    end
    sleep(5.0)
  end
end

check_usb(input_dir)

switch=PiPiper::Pin.new(:pin => 20, :direction => :in)
led=PiPiper::Pin.new(:pin => 17, :direction => :out)
loop do
  time=Time.now
  time_past=time.strftime("%Y%m%d")
  switch.read
  if switch.on? then
    time=Time.now
    tstring=time.strftime("%Y%m%d_%H%M%S")
    led.on
    `sudo ruby /home/pi/git/efmlogger/scripts/read_mcp.rb >> #{input_dir}/#{tstring}.csv &`
    loop do
      time=Time.now
      time_now=time.strftime("%Y%m%d")
      switch.read
      if switch.off? then
        `pkill -f read_mcp`
        led.off
        time_past=time_now
        break
      elsif time_now!=time_past then
        `pkill -f read_mcp`
        time_past=time_now
        break
      end
      time_past=time_now
      sleep(5.0)
    end
  else
    led.off
    sleep(5.0)
  end
end
