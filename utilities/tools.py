import time
import json


def timestamp():
    """
    This is a short function definition that will provide timestamp
    in the form of a string with the format: 'yyyy.mm.dd_hh.mm.ss'.
    """
    now = time.localtime()
    try:
        stamp = str(f'{now.tm_year}.{now.tm_mon}.{now.tm_mday}'
                        f'_{now.tm_hour}.{now.tm_min}.{now.tm_sec}')
    return stamp


def aciFaultDisect(infile):
    """This function expects an ACI fault file in JSON format and will return a list of tuples with the
    (fault_code, fault_severity, fault_description"""
    try:
        with open(infile, "r") as file:
            data = json.load(file)
        imdata = data["imdata"]
        item_key = list(imdata[0].keys())
        attributes = [item[item_key[0]]["attributes"] for item in imdata]
        code_list = [tuple([item["code"], item["severity"], item["descr"]]) for item in attributes]
        return code_list

    except Exception as error:
        print("Error reading JSON file: ", error)


def sortTuple(tup):
    try:
        # reverse = None (Sorts in Ascending order)
        # key is set to sort using second element of
        # sublist lambda has been used
        tup.sort(key=lambda x: x[1], reverse=True)
        return tup

    except Exception as error:
        print("Error sorting tuple: ", error)
