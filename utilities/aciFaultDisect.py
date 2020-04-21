import json


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