def reculsive(x):

    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        return reculsive(x-1) + reculsive(x-2)
