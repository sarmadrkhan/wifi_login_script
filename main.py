import os
import subprocess

def check_and_run():
    # Check if loginDetails.yml exists
    if not os.path.isfile("loginDetails.yml"):
        # Run createYAML.py
        subprocess.run(["python", "createYAML.py"])

    # Run login.py
    subprocess.run(["python", "login.py"])

# Call the function to check and run
check_and_run()
