def number(lines):
    # make a new list
    orderList = []
    newItem = ""
    count = 0
    # for each new item, put it in the list with the number, wrap it with string
    for l in lines:
        count += 1
        newItem = f"{count}: {l}"
        # import it into the new list
        orderList.append(newItem)
    # return list
    return orderList