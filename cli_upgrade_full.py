# CLI Upgrade Script
# Written by Jacob F. (https://www.github.com/FiveEyeTea) on 1/5/2026
# This simple script checks for upgrades with both Winget and Chocolatey. If it detects any, it will run the full upgrade commands for both package managers.
# Winget and Chocolatey must be installed and properly set up before using.

# Initiates the subprocess module
from subprocess import run

# Script header
print("CLI Upgrade Script by Jacob F. (https://www.github.com/FiveEyeTea)")

# Initial checks, stored as individual variables
winget_check = run(["winget", "upgrade"])
choco_check = run(["choco", "upgrade", "all"])

# Checks if the return code is positive. If it is, it will run the full upgrade command.
if winget_check.returncode == 1:
    run(["winget", "upgrade", "-r"])
else:
    print("No Winget upgrades found.")

# Same exact check but for Chocolatey, instead.
if choco_check.returncode == 1:
    run(["choco", "upgrade", "all", "-y"])
else:
    print("No Chocolatey upgrades found.")