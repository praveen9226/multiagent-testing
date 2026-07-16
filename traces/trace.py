import json

def trace(step,status):
    print(json.dumps({'step':step,'status':status}))
