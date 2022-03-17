import json
import sys
import datetime
import base64
import re



#Split up the tactics in individual sessions, we can make new files.
def splitTactics(fulljson):
    resultDict = dict()

    #Fetch steps from the json
    outersteps = fulljson['steps']
    for step in outersteps.keys():
        innerstepkey = step
    innersteps = outersteps[innerstepkey]['steps']


    # Make dictionary of step for each ability id.
    for step in innersteps:
        resultDict[step['ability_id']] = step
    return resultDict
        

#TODO: This all need to be decided on.
#Shows what target the tactic is being executed on.
def getTarget():
    targetDict = dict()
    targetDict['host'] = "parag00n"
    targetDict['ip'] = "1.1.1.1"
    targetDict['path'] = "PATH=C:"
    targetDict['user'] = "parag00n - improg00n"
    return targetDict

#Takes the ability and extract the execution data.
def execData(data):
    execDict = dict()
    execDict['execution-command'] = data['name']
    execDict['execution-id'] = "parag00n drip" #TODO: figure out what we want here. Hash dict?
    execDict['execution-source'] = "Caldera - " + data['name'] #"Caldera - Improsec"
    execDict['execution-category'] = { "name" : "Caldera - Improsec", "abbreviation" : "ci"}
    execDict['target'] = getTarget()
    execDict['time-generated'] = data['finish'] #FIX: need to work no matter what
    if execDict['time-generated'] == None:
        execDict['time-generated'] = "0000-00-00T00:00:00.000Z"
    return execDict

def steps(step):
    stepDict = dict()
    stepDict['command'] = base64.b64decode(step['command']).decode('utf-8')
    stepDict['executor'] = step['executor']
    stepDict['order'] = 1         #TODO: fix if multiple steps.
    date_time_str = step['agent_reported_time']
    x = datetime.datetime.strptime(date_time_str, "%Y-%m-%d %H:%M:%S")
    y = x.isoformat() + ".000Z"
    stepDict['time-start'] = y
    stepDict['time-stop'] = y
    stepDict['output'] = [{ "content" : "todo", "level" : "no info", "type" : "no info"}]
    return [stepDict]


#Multiple abilities in this? Unsure. Atm this just makes a procedure for one step
#Takes the ability and extracts all procedure data.
def procs(step):
    procDict = dict()
    procDict['procedure-name'] = step['name']
    procDict['procedure-description'] = step['description']
    procDict['procedure-id'] = { "type" : "improsec", "id" : "webForKenni"}       #TODO: Fix this?
    procDict['mitre-technique-id'] = step['attack']['technique_id']
    procDict['order'] = 1             #TODO: fix if we want multiple procedures.
    procDict['steps'] = steps(step)
    return procDict



def outputJson(data, steps):
    #Create dict and inset version, execution data and procedures.
    output = dict()
    output['attire-version'] = "1.1"
    output['execution-data'] = execData(data)
    output['procedures'] = []
    for step in steps:
        output['procedures'].append(procs(steps[step]))
    return output

    


def main(arg):
    f = open(arg)

    data = json.load(f)

    #split input into seperate abilities
    abilities_dict = splitTactics(data)
    
    # Create output json for each ability and dump them to files.
        
    out = outputJson(data, abilities_dict)
    out_file = open(re.split(', |_|-|!', arg)[0] + ".json", "w")
    json.dump(out, out_file, indent = 4)
    return 1



if __name__ == "__main__":
   main(sys.argv[1])
