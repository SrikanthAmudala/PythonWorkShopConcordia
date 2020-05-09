def sampleFunRecur(num):
    if num <= 1:
        return 1  # base condition
    else:  # recursive loop
        sumn = num * sampleFunRecur(num-1)
    return sumn

sampleFunRecur(5)