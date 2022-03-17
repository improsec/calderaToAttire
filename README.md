# CalderaToAttire project.
### Purpose
This project is aimed at taking Operation results from caldera and converting them to the ATTiRe logging format, for use in vectr.

### How to use
First run your caldera operation and generate the full operation report in the json format.

CalderaToAttire.py is used to take an entire operation and convert to a single ATTiRe file, directly meaning it will be a single campaign in VECTR. CalderaAbilitiesToAttire.py is used to take each ability in an operation to an individual ATTiRe file, meaning we get multiple campaigns in VECTR.

To run the file, run:
```
python3 CalderaToAttire.py your-report.json
```

To import the file to VECTR, go to the campaign dashboard of the assesment you are currently running.
Click on the 'ASSESMENT ACTIONS' -> 'Import Log' and import your data.

