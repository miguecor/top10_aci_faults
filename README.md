# top10_aci_faults
A script that generates a CSV file from a JSON file gathered from a Cisco ACI APIC.

INFO:
This script provides a list of the top 10 faults (by default) in the ACI fabric.  The number of faults to be shown can be changed with the '--count' or '--all' arguments.  If both arguments are provided '--all' will be preferred.

HELP:
To see the script usage type 'python3 top10_aci_faults.py -h' and the help message will be displayed.

REQUIREMENTS:
No additional modules need to be installed to run this script so there's no 'requirements.txt' file.
