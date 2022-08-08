def is_power_of_four(number: int) -> bool:
	if number == 1:
		return True
	base = 4
	while base <= number:
		if base == number:
			return True
		base *= 4
	return False

print(is_power_of_four(int(input())))