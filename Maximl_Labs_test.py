Total_chars = 256

def max_dis_char(str, a): 

	count = [0] * Total_chars 
	
	for i in range(a): 
		count[ord(str[i])] += 1
	
	maxium_distinct = 0
	for i in range(Total_chars): 
		if (count[i] != 0): 
			maxium_distinct += 1	
	
	return maxium_distinct 

def small_max(str): 

	a = len(str)

	maxium_distinct = max_dis_char(str, a) 
	minl = a
	
	for i in range(a): 
		for j in range(a): 
			subs = str[i:j] 
			subs_l = len(subs) 
			sub_dis_char = max_dis_char(subs, 
												subs_l) 
			
			if (subs_l < minl and
				maxium_distinct == sub_dis_char): 
				minl = subs_l 

	return minl 

if __name__ == "__main__": 
	str = input()
	l = small_max(str); 
	print(l) 
