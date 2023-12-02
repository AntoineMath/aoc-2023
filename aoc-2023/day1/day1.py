numbers = {"one": 1, 
        "two": 2,
        "three":3,
        "four": 4,
        "five":5,
        "six":6,
        "seven":7,
        "eight":8, 
        "nine":9}

min_len_str = 3
max_len_str = 5

with open("aoc1.txt") as f:
    res = 0
    for l in f.readlines():
        l = l.strip()
        left_ptr, right_ptr = 0, len(l)-1
        left_digit, right_digit = "", ""
        found_left, found_right = False, False

        while left_ptr < right_ptr and (not found_left or not found_right): 
            if not found_left:
                if l[left_ptr].isdigit():
                    left_digit = l[left_ptr]
                    found_left = True
                else:
                    for i in range(min_len_str, max_len_str+1):
                        word = l[left_ptr:left_ptr+i]
                        if word in numbers:
                            left_digit = str(numbers[word])
                            found_left = True
                            break
            if not found_left:
                left_ptr += 1

            if not found_right:
                if l[right_ptr].isdigit():
                    right_digit = l[right_ptr]
                    found_right = True
                else:
                    for i in range(min_len_str, max_len_str+1):
                        word = l[right_ptr-i+1:right_ptr+1]
                        if word in numbers:
                            right_digit = str(numbers[word])
                            found_right = True
                            break
            if not found_right:
                right_ptr -= 1

        if left_ptr == right_ptr: 
            if l[left].isdigit():
                res+=int(l[left_ptr]*2)
        else:
            if found_left or found_right:
                temp = ""
                if found_left:
                    temp += left_digit
                if found_right:
                    temp += right_digit
                res+=int(temp)
    print(res)
