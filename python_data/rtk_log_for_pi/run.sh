#!/bin/bash
declare -i usb_flag1=0
declare -i usb_flag2=0
#usb_flag1=0
#usb_flag2=0
while true; do
    sleep 1
#sudo python ./ublox_com.py &
    if [ ! -e "/dev/ttyUSB0" ]; then
	echo can not find ttyUSB0
    elif [ $usb_flag1 != 1 ]; then
	sudo echo find ttyUSB0
	#sudo python ublox_log.py & 
	sudo python user_uart.py &
	sudo python debug_uart.py &
	sudo python rtcm_uart.py &
	#sudo python novatel_pi.py
	#break
	let "usb_flag1=1"
	#$usb_flag1=1
	fi
     	
    if [ ! -e "/dev/ttyUSB4" ]; then 
	    echo can not find ttyUSB4
    elif [ $usb_flag2 != 1 ]; then
	echo find ttyUSB4
	let "usb_flag2=1"
	sudo python novatel_pi.py &
	#sudo python ./user_uart.py &
	#sudo python ./debug_uart.py &
	#sudo python ./rtcm_uart.py &
    fi
    if [ $usb_flag1 == 1 -a $usb_flag2 == 1 ]; then 
	    echo find all
	    break
    fi


done
# sudo python ./user_uart.py &
# sudo python ./debug_uart.py &
# sudo python ./rtcm_uart.py &

# sudo python ./ublox_log.py &
