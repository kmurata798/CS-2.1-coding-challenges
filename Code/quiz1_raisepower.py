def raise_power(base, exp):
    if (exp==1):
        return base
    else:
        return base*raise_power(base, exp-1)


print("Answer:", raise_power(3, 3))