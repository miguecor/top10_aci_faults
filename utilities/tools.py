import sys
import time
import json


def aciFaultDisect(infile):
    """This function expects an ACI fault file in JSON format and will return a list of tuples with the
    (fault_code, fault_severity, fault_description"""
    try:
        with open(infile, "r") as file:
            data = json.load(file)
        imdata = data["imdata"]
        if len(imdata) == 0:
            print("\nThe file %s does not contain any faults." % infile)
            input("\nHit Enter to end script. ")
            sys.exit(0)
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
