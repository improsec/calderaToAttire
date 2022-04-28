# CalderaToAttire project.
### Purpose
This project is aimed at taking Operation results from caldera and converting them to the ATTiRe logging format, for use in vectr.

### How to use
First run your caldera operation and generate the full operation report with userinput in json format.

CalderaToAttire.py is used to take an entire agent and convert to a single ATTiRe file. Meaning it will be a single campaign in VECTR for each agent.

To run the file, run:
```
python3 CalderaToAttire.py your-report.json
```

To import the file to VECTR, go to the campaign dashboard of the assesment you are currently running.
Click on the 'ASSESMENT ACTIONS' -> 'Import Log' and import your data.

### Authors
Philip Kreutzer
