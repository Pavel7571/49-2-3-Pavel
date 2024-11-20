numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим


known_numbers = [num for num in numbers if num is not None]

average = sum(known_numbers) / (len(known_numbers) + 1)
numbers[numbers.index(None)] = average
print("Измененный список:", numbers)
