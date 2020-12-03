def two_sum():
    compliments = {}
    file = open("input.txt", "r")
    for line in file.readlines():
        line = int(line)
        if line in compliments:
            return (2020-line)*line
        compliments[2020-line] = 0


def three_sum():
    nums = []
    file = open("input.txt", "r")
    for line in file.readlines():
        nums.append(int(line))

    for i in nums:
        for j in nums:
            for k in nums:
                if i+j+k == 2020:
                    return (i*j*k)



print(two_sum())
print(three_sum())