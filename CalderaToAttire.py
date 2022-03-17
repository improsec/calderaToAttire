import json
import sys
import datetime
import base64



#Split up the tactics in individual sessions, we can make new files.
def splitAgents(fulljson):
    resultDict = dict()

    #Fetch steps from the json
    outersteps = fulljson['steps']
    agents = outersteps.keys()

    for agent in agents:
        resultDict[agent] = outersteps[agent]['steps']
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
def execData(data, agent):
    execDict = dict()
    execDict['execution-command'] = data['name']
    execDict['execution-id'] = agent #Might be a better possbility
    execDict['execution-source'] = "Caldera - " + data['name'] + " - " + agent
    execDict['execution-category'] = { "name" : "Caldera - Improsec", "abbreviation" : "ci"}
    execDict['target'] = getTarget()
    execDict['time-generated'] = data['finish'] 
    if execDict['time-generated'] == None:
        execDict['time-generated'] = "0000-00-00T00:00:00.000Z"
    return execDict

def steps(step, index):
    stepDict = dict()
    stepDict['command'] = base64.b64decode(step['command']).decode('utf-8')
    stepDict['executor'] = step['executor']
    stepDict['order'] = index
    date_time_str = step['agent_reported_time']
    x = datetime.datetime.strptime(date_time_str, "%Y-%m-%d %H:%M:%S")
    y = x.isoformat() + ".000Z"
    stepDict['time-start'] = y
    stepDict['time-stop'] = y
    output = "Empty"
    if 'output' in step.keys(): 
        output = step['output']
    stepDict['output'] = [{ "content" : output, "level" : "no info", "type" : "no info"}]
    return [stepDict]


#Takes one ability and extracts one procedure.
def procs(step, index):
    procDict = dict()
    procDict['procedure-name'] = step['name']
    procDict['procedure-description'] = step['description']
    procDict['procedure-id'] = { "type" : "improsec", "id" : "webForKenni"}       #TODO: Fix this?
    procDict['mitre-technique-id'] = step['attack']['technique_id']
    procDict['order'] = index
    procDict['steps'] = steps(step, index)
    return procDict


# Create the output json for a single agent.
def outputJson(data, agentDict, agent):
    output = dict()
    output['attire-version'] = "1.1"
    output['execution-data'] = execData(data, agent)
    output['procedures'] = []
    for index, ability in enumerate(agentDict):
        output['procedures'].append(procs(ability, index))
    return output

# Loops over all agents and outputs them to files.
def outputAgent(fulldata, agentDict, agent):
    out = outputJson(fulldata, agentDict, agent)
    out_file = open("ATTiRe - " + agent +".json", "w")
    json.dump(out, out_file, indent = 4)
    return


def main(arg):
    f = open(arg)

    data = json.load(f)

    agentDict = splitAgents(data)
    for agent in agentDict:
        outputAgent(data, agentDict[agent], agent)
    
    return



if __name__ == "__main__":
   main(sys.argv[1])
