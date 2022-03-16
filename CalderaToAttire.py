import json
import sys#, getopt

#Split up the tactics in individual sessions, we can make new files.
def splitTactics(fulljson):
    resultDict = dict()

    #Fetch steps from the json
    outersteps = fulljson.get('steps')
    for i in outersteps.keys():
        innerstepkey = i
    innersteps = outersteps.get(innerstepkey).get('steps')


    # Make dictionary of step for each ability id.
    techniques = []
    for step in innersteps:
        techniques.append(step.get('ability_id'))
        resultDict[step.get('ability_id')] = step
    return resultDict
        

    #print (resultDict.get('90c2efaa-8205-480d-8bb6-61d90dbaf81b'))

#TODO: This all need to be decided on.
#Shows what target the tactic is being executed on.
def getTarget(step):
    targetDict = dict()
    targetDict['host'] = "parag00n"
    targetDict['ip'] = "1.1.1.1"
    targetDict['path'] = "PATH=C:"
    targetDict['user'] = "parag00n - improg00n"

#Takes the ability and extract the execution data.
def execData(step):
    #print(inp)
    execDict = dict()
    execDict['execution-command'] = step.get('command')  #TODO: decode base64?
    execDict['execution-id'] = "parag00n drip" #TODO: figure out what we want here. Hash dict?
    execDict['execution-source'] = "Caldera - Improsec"
    execDict['execution-category'] = { "name" : "Caldera - Improsec", "abbreviation" : "ci"}
    
    execDict['target'] = getTarget(step)

    execDict['time-generated'] = step.get('agent_reported_time')
    return execDict

def steps(step):
    stepDict = dict()
    stepDict['command'] = step.get('command') #TODO: decode base64
    stepDict['executor'] = step.get('executor')
    stepDict['order'] = "1"         #TODO: fix if multiple steps.
    stepDict['time-start'] = step.get('agent_reported_time')
    stepDict['time-stop'] = "unknown"
    stepDict['output'] = { "content" : "todo", "level" : "no info", "type" : "no info"}
    return [stepDict]


#Multiple abilities in this? Unsure. Atm this just makes a procedure for one step
#Takes the ability and extracts all procedure data.
def procs(step):
    procDict = dict()
    procDict['procedure-description'] = ""
    procDict['procedure-id'] = { "type" : "improsec", "id" : "webForKenni"}       #TODO: Fix this?
    procDict['mitre-technique-id'] = step.get('attack').get('technique_id')
    procDict['order'] = "1"             #TODO: fix if we want multiple procedures.
    procDict['steps'] = steps(step)
    return [procDict]



def outputJson(step):
    #Create dict and inset version, execution data and procedures.
    output = dict()
    output['attire-version'] = "1.1"
    output['execution-data'] = execData(step)
    output['procedures'] = procs(step)

    #Output the json
    #print(json.dumps(output, indent = 4))
    return output

    


def main(arg):
    f = open(arg)

    data = json.load(f)

    dict1 = splitTactics(data)
    
    for i in dict1:
        #print(dict1[i])
        out = outputJson(dict1[i])
        out_file = open(i + ".json", "w")
        json.dump(out, out_file, indent = 4)
        break


    return 1





if __name__ == "__main__":
   main(sys.argv[1])
