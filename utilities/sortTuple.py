def sortTuple(tup):
    try:
        # reverse = None (Sorts in Ascending order)
        # key is set to sort using second element of
        # sublist lambda has been used
        tup.sort(key=lambda x: x[1], reverse=True)
        return tup

    except Exception as error:
        print(error)