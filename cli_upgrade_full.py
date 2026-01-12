# CLI Upgrade Script
# Initially written by Jacob F. (https://www.github.com/FiveEyeTea) on 1/5/2026.
# This simple script checks for upgrades with both Winget and Chocolatey. If it detects any, it will run the full upgrade commands for both package managers.
# NOTE: Winget and Chocolatey must be installed and properly set up before using. 
# Chocolatey portion of the script only upgrades software installed with Chocolatey. 
# Winget portion will attempt to upgrade all software on the system, provided it's compatible with Winget.

# Script header
print("CLI Upgrade Script by Jacob F. (https://www.github.com/FiveEyeTea)")

# Initiates the subprocess module for the run statements. Crucial for running all the winget/choco commands.
from asyncio import subprocess
from subprocess import run

# Initial checks, stored as individual variables. This would be considered a "dry run", this part doesn't actually upgrade anything. It's only used to check the return code.
winget_check = run(["winget", "upgrade"])
choco_check = run(["choco", "upgrade", "all", "-n"])

# This variable is the upgrade command processes for Winget. It only activates if updates are found.
# NOTE: The "agreements" flags are merely meant for automation. If you don't want the script to automatically accept the agreements, use cli_upgrade_noagree.py instead.
winget_upgrade = run([
    "winget",
    "upgrade",
    "--all",
    "--accept-source-agreements",
    "--accept-package-agreements",
])

# The following print statement is for debugging only: print(winget_check.returncode, choco_check.returncode)

# Checks if the return code is positive. If the return code is 1, it will run the upgrade process in Winget.
if winget_check.returncode == 1:
    run(subprocess.run(winget_upgrade, text=True))
elif winget_check.returncode == 0:
    print("\nNo applicable Winget upgrades found.")
else:
    print("ERROR: No return code specified.")

# Same exact check but for Chocolatey, instead.
if choco_check.returncode == 1:
    run(["choco", "upgrade", "all", "-y"])
elif choco_check.returncode == 0:
    print("No applicable Chocolatey upgrades found.\n")
else:
    print("ERROR: No return code specified.")
