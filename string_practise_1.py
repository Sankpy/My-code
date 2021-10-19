def first_and_last(massage):
    massage_lenth=len(massage)
    if massage_lenth==0:
        return True
    first_index=massage[0]
    last_index=massage[massage_lenth-1]
    if first_index==last_index:
        return True
    else:
        return False
print(first_and_last("else"))
print(first_and_last("tree"))
print(first_and_last(""))