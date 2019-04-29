def check_speed(speed):
	if speed < 70:
		print("okay")
	else:
		speed = speed - 70
		points = speed // 5
		if points < 12:
			print(points)
		else:
			print("License Suspended")

speed = int(input("Enter the speed:"))
check_speed(speed)
