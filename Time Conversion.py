def time_conversion(time):
	if time[0] == "1" and time[1] == "2" and int(time[3]) == 0 and not int(time[4]) > 0 and time[-2] == "A":
			print("00:00:00")
	elif time[0] == "1" and time[1] == "2" and int(time[3]) == 0 and not int(time[4]) > 0 and time[-2] == "P":
			print("12:00:00")
	elif time[8] == "A" and time[0] == "1" and time[1] == "2":
		    print("00" +  time[2:8])
	elif time[8] == "A":
			print(time[:8])
	elif time[0] == "1" and time[1] == "2" and time[8] == "P":
		    print(time[:8])
	else:
			num1 = int(time[0])
			num2 = int(time[1])
			num3 = num1 * 10 + num2
			num4 = num3 + 12
			print(str(num4) + time[2:8])

time = input()
time_conversion(time)
