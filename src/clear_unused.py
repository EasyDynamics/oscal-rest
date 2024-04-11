import yaml

working_dir = "../"
input_file = working_dir + "/OSCALRestOpenAPI.yaml"
output_file = working_dir + "/OSCALRestOpenAPI_REDUCED.yaml"
in_use_file = working_dir + "/rpt_in_use_list.txt"
removed_file = working_dir + "/rpt_removed_list.txt"

ref_list = []
remove_list = []

def build_ref_list(key_name, item_key, item_value):
    if item_key == key_name:
        if item_value[0] == "#" and (item_value not in ref_list) :
            print("+", end="")
            ref_list.append(item_value)
        else:
            print("_", end="")
    else:
        print(".", end="")

def lookup(key_name, data):
    global ref_list
    if isinstance(data, dict):
        for item_key, item_value in data.items():
            if isinstance(item_value, dict):
                lookup(key_name, data[item_key])
            else: # isinstance(item_value, list):
                build_ref_list(key_name, key_name, item_value)


def interrogate(top_level_key_name):
    global ref_list
    print("-- Checking " + top_level_key_name)
    lookup("$ref", openAPI[top_level_key_name])
    print()

with open(input_file, 'r') as file:
    openAPI = yaml.safe_load(file)

print("Compiling list of references in use")
interrogate("tags")
interrogate("paths")

with open(in_use_file, 'w') as file:
        for line in ref_list:
            file.write("%s\n" % line)

print("Identifying schema definitions to remove")
for item in openAPI["components"]["schemas"].keys():
    if not "#/components/schemas/" + item in ref_list: 
        remove_list.append(item)

with open(removed_file, 'w') as file:
        for line in remove_list:
            file.write("%s\n" % line)

for item in remove_list:
    del openAPI["components"]["schemas"][item]
        
with open(output_file, 'w') as file:
    yaml.dump(openAPI, file, sort_keys=False)

