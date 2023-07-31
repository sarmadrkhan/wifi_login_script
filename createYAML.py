import yaml

# Prompt user for input
username = input("Enter user id e.g ABCXYZ99@edisu-piemonte.it: ")
password = input("Enter password: ")

# Create dictionary with user input
data = {
    "wifi_user": {
        "userid": username,
        "password": password,
    },
    "url": "http://10.12.16.1:8002/index.php?zone=cpzone&redirurl=http%3A%2F%2Fwww.msftconnecttest.com%2Fredirect"
}

# Save data to YAML file
with open("loginDetails.yml", "w") as file:
    yaml.dump(data, file)
