import json
with open('sampledata.json','r') as file:
    data=json.load(file)
print("Interface Status")
print("================================================================================")
print("DN                                                 Description           Speed    MTU  ")
print("-------------------------------------------------- --------------------  ------  ------")
for i in range(len(data["imdata"])):
    print(data["imdata"][i]["l1PhysIf"]["attributes"]["dn"],'                              ',data["imdata"][i]["l1PhysIf"]["attributes"]["speed"],'   ',data["imdata"][i]["l1PhysIf"]["attributes"]["mtu"])