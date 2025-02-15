import json 


print("Interface status")
print("================================================================================")
print("DN                                                 Description           Speed    MTU  ")
print("-------------------------------------------------- --------------------  ------  ------")

with open('json/sample-data.json') as f:
    data = json.load(f)

main=data['imdata']
for i in main:
    name=i['l1PhysIf']
    att=name['attributes']
    dn=att['dn']
    speed=['speed']
    mtu=['mtu']
    print(dn, "                            ", speed," ", mtu )