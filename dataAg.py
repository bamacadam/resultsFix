import json

path = "../data/math_results_"
name = lambda x: path + (str (x)) + ".json" 
files = [json.load(open(name(x))) for x in range(0,64)]
rawData = [{'u':datum['u'], 'v':datum['v'], 's':datum['s'], 't':datum['t']} 
            for f in files for datum in f if datum]
##print(rawData)
a = open("data1.json", "w")
json.dump(rawData,a)
