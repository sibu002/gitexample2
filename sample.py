import yaml

# Load the YAML file
with open("sample.yaml", "r") as file:
    try:
        data = yaml.safe_load(file)
    except yaml.YAMLError as exc:
        print(exc)
        exit()

# Print the contents
print(data)
