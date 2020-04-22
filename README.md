# top10_aci_faults
## A script that generates a CSV file from a JSON file gathered from a Cisco APIC.

This script will generate a CSV file with the following structure:
`fault, count, severity, description`

The output file will be put in the same folder as the script. By default, the output file will be named:
`ACI_faults_<aaaa.mm.dd_hh.mm.ss>.csv`

### JSON FILE
To obtain the JSON file necessary to run this script you need to be connected to the Cisco APIC either via CLI or GUI.

- From the GUI:
  - Go to __System > Faults__:
    - Click on the '__Download__' icon at the top right corner under the question mark (?) icon.
      - At 'Content' choose '__All Properties__'.
      - At 'Export Format' choose '__json__'.
      - Click on '__Download__'

- From the CLI:
  - SSH into the APIC and enter the command:
    - `# moquery -c fault.Inst -o json >> /Users/<username>/<filename.json>`
      - Get the file using your preferred SFTP/SCP client.

### USAGE
The script can be used in the following ways:

- Top 10 faults by count (default):
  - `$ python3 top10_aci_faults.py <filename.json>`

- Get all the faults:
  - `$ python3 top10_aci_faults.py <filename.json> --all`

- Get top _x_ number of faults (_x_ is an integer >= 1):
  - `$ python3 top10_aci_faults.py <filename.json> --count <x>`

- To give a specific name for the output file:
  - `$ python3 top10_aci_faults.py <filename.json> --output <custom_output_filename.csv>`

Any of the arguments (`--count`, `--all` or `--output`) can be used in a mix.  If you type `--all` and `--count`, `--all` will be preferred.

### HELP
There’s also a help menu to understand how to use the script.

- To show the help menu:
  - `$ python3 top10_aci_faults.py -h`

### REQUIREMENTS
This script does not use any modules outside your default Python3 implementation.  That's why a `requirements.txt` file has not been provided.

### IMPORTANT
The description of a fault is not generic.  Meaning that it does not provide information for all the faults of the type.  The description was gathered from only one of the faults of the type in the JSON file.  It’s supposed to give us an idea of how to tackle each one of the different fault codes.

I’m working on creating a dictionary with a recommendation of how to fix any particular fault that can be of more help.  But in the meanwhile, I hope this script makes our lives a little easier.
