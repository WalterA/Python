def moltiplica_numeri(numbers: list[int], threshold: int) -> int:
    temp=0
    for i in numbers:
        if i < threshold:
            if temp:
                if i < threshold:
                    temp*=i
            else:
                temp=i
    if temp:
        return temp
    else:
        return 1