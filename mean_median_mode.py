#Calculates the mean, median, and mode of a list of numbers:

#Gets sum of nums and divides them by len(nums)
def mean(nums):
    num_sum = 0
    for num in nums:
        num_sum += num
    #Determines how many decimal places to round answer to
    decimals = int(input('How many decimal places would you like to round your mean to? ' ))
    mean = round((num_sum/len(nums)), decimals)
    print('The mean is: ', mean)
    return mean


#Calculates and returns a 'list' with just the median of nums
def median(nums):
    median = []
    nums = sorted(nums)
    if len(nums) % 2 == 1:
        median = median + [nums[int(len(nums)/2)]]
    else:
        median = median + [nums[int(len(nums)/2)]] + [nums[int(len(nums)/2)+1]]
    if len(median) == 1:
        print('The median number is: ', median)
    else:
        print('The median numbers are: ', median)
    return median


#Calculates the mode. 
def mode(nums):
    freq = {}
    mode = []
    #Creates a dictionary to determine the frequency of each number in nums
    for num in nums:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    #Determines the dictionary key (number) that occurs the most frequently.
    mode_values = sorted(freq.items(), key = lambda x : x[1], reverse = True)
    top = mode_values[0][1]
    for i in mode_values:
        if i[1] == top:
            mode = mode + [i[0]]
    #Prints appropriate statement
    if len(mode) == 1:
        print('The mode is: ', mode)
    else:
        print('The modes are: ', mode)
    return(mode)
    


#Whole thing!
def whole_prog():
    numnums = int(input('Enter how many numbers are in your list: '))
    #Setting up the list of nums for all functions
    nums = []
    for i in range(numnums):
        num = float(input('Enter your next number: '))
        nums.append(num)
    print('Your list of nums is: ', nums)
    print('\n')
    mean(nums)
    median(nums)
    mode(nums)
    return 'That\'s all, folks'

whole_prog()

    
        
