from base_class import uart_class as uart

uart.uart_communicate.print_used_com()
ret = False 

serial = uart.uart_communicate("com15",460800,0.5,True,'123.txt')
if (serial.is_connect):
	serial.recive_data(1)
	serial.log_file_close()