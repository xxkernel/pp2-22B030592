import json
list = []
with open("example.json", 'r') as json_file:
     a = json.load(json_file)
print('Interface Status')
print('='*80)
print('DN'," "*48,"Description"," "*9,'Speed'," "*1,'MTU')
print('-'*50,"",'-'*20,"","-"*6,""*2,"-"*6)
cnt = 0
for i in a["imdata"]:
    if cnt == 3:
        break
    print(json.dumps(i["l1PhysIf"]["attributes"]["dn"]), 
          end="                            ")
    print(json.dumps(i["l1PhysIf"]["attributes"]["speed"]), end = " ")
    print(json.dumps(i["l1PhysIf"]["attributes"]["mtu"]), end = " ")
    print()
    cnt += 1