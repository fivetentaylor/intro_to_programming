def isOneBitCharacter(bits: List[int]) -> bool:
    if len(bits) == 1:
        return True
    if len(bits) < 1:
        return False
    if bits[-1] == 1:
        return False
    if bits[-2] == 0:
        return True
    if bits[-3] == 0:
        return False
    return True

    # 1, 0, 0
    # 0, 1, 0
    # 0, 0, 1, 0
    # 1, 0, 1, 1, 0
    # 0, 1, 1
    # 0, 0, 1, 0
    # 0
