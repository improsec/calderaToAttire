import json
import sys#, getopt

def splitTactics(fulljson):
    outersteps = fulljson.get('steps')
    for i in outersteps.keys():
        innerstepkey = i
    innersteps = outersteps.get(innerstepkey).get('steps')
    for step in innersteps:
        print(step.get('attack').get('technique_name'))
    #print(innersteps)
    


def main(arg):
    f = open(arg)

    data = json.load(f)
    splitTactics(data)


    return 1





if __name__ == "__main__":
   main(sys.argv[1])
