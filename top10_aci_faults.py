#!/usr/bin/python

import argparse
import collections
import re
import sys
from datetime import datetime
from os import getcwd
from utilities.tools import aciFaultDisect, sortTuple


def get_parser():
    try:
        parser = argparse.ArgumentParser(
            usage="python %(prog)s [-h] infile [--count {X}] [--all] [--output {filename}]",
            description="Creates a CSV file with a list of ACI faults from a provided JSON file.")
        parser.add_argument(
            "infile", nargs="?", type=str, default=sys.stdin,
            help="input JSON file generated from an APIC with the command: 'moquery -c fault.Inst -o json'")
        parser.add_argument(
            "--count", type=int, default=10, metavar="X", nargs="?",
            help="use this argument to show [X] number of faults from the provided file (10 by default)")
        parser.add_argument(
            "--all", action="store_true",
            help="use of this argument will provide all the faults from the JSON file")
        parser.add_argument(
            "--outfile", type=str, metavar="filename", nargs="?",
            help="name of the output file to be created (default is 'ACI_faults_aaaa.mm.dd_hh.mm.ss.csv'")
        return parser.parse_args()

    except Exception as error:
        print("Error parsing arguments: ", error)


def get_code_counter(fault_list):
    code_only_list = [(fault[0]) for fault in fault_list]
    code_counter = collections.Counter(code_only_list)
    return code_counter


def number_of_faults_to_show(fault_list, argv_all, argv_count):
    if argv_all is True:
        faults_to_show = len(fault_list)
    else:
        faults_to_show = argv_count
    return faults_to_show


def generate_code_vs_count_list(counter, faults_to_show):
    code_vs_count_list = sortTuple(counter.most_common(faults_to_show))
    return code_vs_count_list


def cross_reference_lists(code_vs_count_list, all_faults_list):
    look_up_dict = {entry[0]: {"severity": entry[1], "description": entry[2]} for entry in all_faults_list}
    final_dict = {entry[0]: {"count": entry[1], "severity": look_up_dict[entry[0]]["severity"],
                             "description": look_up_dict[entry[0]]["description"]} for entry in code_vs_count_list}
    return final_dict


def create_csv(dictionary, new_filename):
    try:
        with open(new_filename, "x+") as csv_file:
            csv_file.write(str("fault,count,severity,description,\n"))
            faults = list(dictionary.keys())
            for fault in faults:
                dictionary[fault].update(description = (re.sub(r"[\ ]{2,}", " ", dictionary[fault]["description"])))
                csv_file.write(f"{fault},{dictionary[fault]['count']},{dictionary[fault]['severity']},"
                               f"\"{dictionary[fault]['description']}\"\n")
        pass

    except Exception as error:
        print("Error creating CSV file: ", error)


def outfile_name(argv_output):
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    default = f"aci_faults_{timestamp}.csv"
    return argv_output or default


def say_goodbye(code_vs_count_list, all_faults_list, filename):
    print("")
    print("Faults read from JSON file:    ".rjust(36), f"{len(all_faults_list)}")
    print("Faults added to CSV file:    ".rjust(36), f"{len(code_vs_count_list)}")
    print("CSV file name:    ".rjust(36), f"{filename}")
    print("Location:    ".rjust(36), f"{getcwd()}\n")
    pass


def main():
    parser = get_parser()
    all_faults_list = aciFaultDisect(parser.infile)
    code_counter = get_code_counter(all_faults_list)
    faults_to_show = number_of_faults_to_show(code_counter, parser.all, parser.count)
    code_vs_count_list = generate_code_vs_count_list(code_counter, faults_to_show)
    final_dict = cross_reference_lists(code_vs_count_list, all_faults_list)
    create_csv(final_dict, outfile_name(parser.outfile))
    say_goodbye(code_vs_count_list, all_faults_list, outfile_name(parser.outfile))
    pass


if __name__ == '__main__':
    main()
