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

    except Exception as val:
        print("Something went wrong!")
        print("Error: ", val)

    return stamp


def aciFaultDisect(infile):
    """This function expects an ACI fault file in JSON format and will return a list of tuples with the
    (fault_code, fault_severity, fault_description"""
    code_list = []
    try:
        with infile:
            json_data = json.load(infile)
            imdata_list = (json_data.get("imdata"))
            for imdata in imdata_list:
                attrib_dict = imdata.get("faultInst")
                code_dict = attrib_dict.get("attributes")
                code_str = (code_dict["code"])
                sev_str = (code_dict["severity"])
                descr_str = (code_dict["descr"])
                code_list.append(tuple([code_str, sev_str, descr_str]))
        return code_list

    except Exception as error:
        print("Error reading file: ", error)


def sortTuple(tup):
    try:
        # reverse = None (Sorts in Ascending order)
        # key is set to sort using second element of
        # sublist lambda has been used
        tup.sort(key=lambda x: x[1], reverse=True)
        return tup

    except Exception as error:
        print(error)
