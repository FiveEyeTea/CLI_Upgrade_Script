# CLI Upgrade Script
# Written by Jacob F. (https://www.github.com/FiveEyeTea) on 1/5/2026
# This simple script checks for upgrades with both Winget and Chocolatey. If it detects any, it will run the full upgrade commands for both package managers.
# Winget and Chocolatey must be installed and properly set up before using.

# Script header
print("CLI Upgrade Script by Jacob F. (https://www.github.com/FiveEyeTea)")

# Initiates the subprocess module for the run statements. Crucial for running all the winget/choco commands.
from subprocess import run

# Initial checks, stored as individual variables.
winget_check = run(["winget", "upgrade"])
choco_check = run(["choco", "upgrade", "all"])

# The following print statement is for debugging only: print(winget_check.returncode, choco_check.returncode)

# Checks if the return code is positive. The "agreements" flags are merely meant for automation. If you don't want the script to automatically accept the agreements, use cli_upgrade_noagree.py instead.
if winget_check.returncode == 1:
    run(["winget", "upgrade", "--all", "--accept-source-agreements", "--accept-package-agreements"])
elif winget_check.returncode == 0:
    print("\nNo applicable Winget upgrades found.")

# Same exact check but for Chocolatey, instead.
if choco_check.returncode == 1:
    run(["choco", "upgrade", "all", "-y"])
else:
    print("No applicable Chocolatey upgrades found.\n")