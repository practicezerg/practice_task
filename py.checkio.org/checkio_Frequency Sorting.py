






def frequency_sorting(numbers: list[int]):
	list_res = []
	json_temp = {}
	for i in numbers:
		if i not in json_temp:
			json_temp[i] = 1
		else:
			json_temp[i] += 1
	print(json_temp)
	return list_res



numbers = [3, 4, 11, 13, 11, 4, 4, 7, 3]
list_res = frequency_sorting(numbers)
#[4,4,4,3,3,11,11,7,13,]
print(list_res)



def frequency_sorting(numbers: list[int]):
    slov = {}
    for num in numbers:
        if num in slov:
            slov[num] += 1
        else:
            slov[num] = 1
    def sort_key(item):
        return (-slov[item], item)
    sorted_data = sorted(numbers, key=sort_key)
    return sorted_data