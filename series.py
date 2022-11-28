#identifies the type and "d" of a series given a list of numbers
def identify(nums: list):
    arith, geo = True, True
    d = nums[1] - nums[0]
    if (nums[0] != 0): a = nums[1] / nums[0]
    else: a = None
    for i, num in enumerate(nums[:-1]):
        if (nums[i+1] - num != d):
            arith = False
        d = nums[i+1] - num
        if (num != 0):
            if (nums[i+1] / num != a):
                geo = False
            a = nums[i+1] / num
    if (arith): return ("arithmetic", float(d))
    elif (geo): return ("geometric", float(a))
    else: return None

#returns list of extrapolated values of an arithmetic series given start value, amnt, and d
def extrapa(startVal: float, amnt: float, d: float):
    nums = []
    for i in range(amnt):
        nums.append(startVal + d * i)
    return nums

#returns list of extrapolated values of an arithmetic series given a list of nums, and amnt
def extrapal(nums: list, amnt: int):
    startVal = nums[0]
    d = identify(nums)[1]
    return extrapa(startVal, amnt, d)

#returns list of extrapolated values of a geometric series given start value, amnt, and d
def extrapg(startVal: float, amnt: float, d: float):
    nums = []
    for i in range(amnt):
        nums.append(startVal * d ** i)
    return nums

#returns list of extrapolated values of a geometric series given a list of nums, and amnt
def extrapgl(nums: list, amnt: int):
    startVal = nums[0]
    d = identify(nums)[1]
    return extrapg(startVal, amnt, d)
