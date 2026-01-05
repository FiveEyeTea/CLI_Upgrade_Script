# CLI Upgrade Script (Winget Only)
# Written by Jacob F. (https://www.github.com/FiveEyeTea) on 1/5/2026
# This simple script checks for upgrades with Winget. If it detects any, it will run the full upgrade commands for both package managers.
# Winget must be installed and properly set up before using.

# Initiates the subprocess module
from subprocess import run

# Script header
print("CLI Upgrade Script (Winget Only version) by Jacob F. (https://www.github.com/FiveEyeTea)")

# Initial check, stored as individual variables
winget_check = run(["winget", "upgrade"])

# Checks if the return code is positive. If it is, it will run the full upgrade command.
if winget_check.returncode == 1:
    run(["winget", "upgrade", "-r"])
else:
    print("No Winget upgrades found.")
