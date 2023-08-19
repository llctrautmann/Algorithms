# return masked string
def maskifylegacy(cc):
    """
    need to take any input
    check the length of the input
    convert any values except the last four into hashtags
    """

    target = str(cc)
    target_length = len(target)
    target_list = [a for a in target]

    for i in range(len(target_list) - 4):
        target_list[i] = "#"

    target_list_tup = tuple(target_list)

    output = "".join(target_list_tup)
    return output


# return masked string IF STRING AS INPUT
def maskify(cc):
    return "#" * (len(cc) - 4) + cc[-4:]
