import sys
import argparse
import collections
from utilities.tools import timestamp, sortTuple, aciFaultDisect

parser = argparse.ArgumentParser(usage="python %(prog)s [-h] infile [--count {X}] [--all] [--output {filename}]",
                                 formatter_class=argparse.RawDescriptionHelpFormatter,
                                 description=("Generates a CSV file with a list of ACI faults from a provided JSON file."))
parser.add_argument("infile", nargs="?", type=argparse.FileType("r"), default=sys.stdin,
                    help="JSON file generated from the APIC with the command: 'moquery -c fault.Inst -o json'")
parser.add_argument("--count", type=int, default=10, metavar="X", nargs="?",
                    help="use this argument to show [X] number of faults from the provided file (10 by default)")
parser.add_argument("--all", action="store_true",
                    help="use of this argument will provide all the faults from the JSON file")
parser.add_argument("--output", type=str, default="ACI_faults", metavar="filename", nargs="?",
                    help="name of the output file to be generated (default is 'ACI_faults_aaaa.mm.dd_hh.mm.ss.csv'")
args = parser.parse_args()

aci_faults_json = args.infile

fault_list = final_fault_list = []

raw_fault_list = aciFaultDisect(aci_faults_json)

for fault_entry in raw_fault_list:
    fault_list.append(fault_entry[0])

aci_faults_count = collections.Counter(fault_list)

if args.all is True:
    fault_list = aci_faults_count.most_common(len(raw_fault_list))
else:
    fault_list = aci_faults_count.most_common(args.count)
sorted_list = (sortTuple(fault_list))

if args.output == "ACI_faults":
    output_filename = f"{args.output}_{timestamp()}.csv"
else:
    output_filename = args.output

with open(output_filename, "x+") as file:
    file.write(str("fault,count,severity,description,"))
    file.write("\n")
    for fault in sorted_list:
        for raw_fault in raw_fault_list:
            if fault[0] is raw_fault[0]:
                file.write(str(f"{fault[0]},{fault[1]},{raw_fault[1]},\"{raw_fault[2]}\","))
                file.write("\n")

print(f"\nEnd of script.\n"
      f"A total of {len(sorted_list)} faults included in file \'{output_filename}\'.\n")
