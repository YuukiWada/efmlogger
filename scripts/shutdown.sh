#!/bin/sh

if [ ! -e /sys/class/gpio/gpio21 ]; then
    echo "21" > /sys/class/gpio/export
    echo "in" > /sys/class/gpio/gpio21/direction
fi

while [ 1 = 1 ]
do
    value=`cat /sys/class/gpio/gpio21/value`
    if [ $value -eq "1" ] ; then
	sleep 1
	value=`cat /sys/class/gpio/gpio21/value`
	if [ $value -eq "1" ] ; then
	    sudo shutdown -h now
	fi
    fi
    sleep 1
done
