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
def getTarget(inp):
    targetDict = dict()
    targetDict['host'] = "parag00n"
    targetDict['ip'] = "1.1.1.1"
    targetDict['path'] = "PATH=C:"
    targetDict['user'] = "parag00n - improg00n"

def execData(inp):
    #print(inp)
    execDict = dict()
    execDict['execution-command'] = inp.get('command')  #TODO: decode base64?
    execDict['execution-id'] = "solarflare drip" #TODO: figure out what we want here. Hash dict?
    execDict['execution-source'] = "Caldera - Improsec"
    execDict['execution-category'] = { "name" : "Caldera - Improsec", "abbreviation" : "ci"}
    
    execDict['target'] = getTarget(inp)

    execDict['time-generated'] = inp.get('agent_reported_time')
    return execDict

def procs(inp):
    return



def outputJson(inp):
    #Create dict and inset version, execution data and procedures.
    output = dict()
    output['attire-version'] = "1.1"
    output['execution-data'] = execData(inp)
    output['procedures'] = procs(inp)

    #Output the json
    print(json.dumps(output, indent = 4))
    return 1

    


def main(arg):
    f = open(arg)

    data = json.load(f)

    dict1 = splitTactics(data)
    
    for i in dict1:
        #print(dict1[i])
        outputJson(dict1[i])
        break


    return 1





if __name__ == "__main__":
   main(sys.argv[1])
