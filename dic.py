living_storage ={"a":"dryer","b":"toy ship","c":"seaw dagha","d":"tool box"}
print(living_storage["d"] +  living_storage["b"])
print(living_storage.keys())
print(living_storage.values())
print(living_storage.update({"c":"family album"}))
print(living_storage)
living_storage["d"]="camera"
print(living_storage)
living_storage.pop("c")
print(living_storage)
living_storage["e"]="christmas tree"
print(living_storage)
print(living_storage.pop)

