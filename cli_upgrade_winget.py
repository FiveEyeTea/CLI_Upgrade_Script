# CLI Upgrade Script
# Initially written by Jacob F. (https://www.github.com/FiveEyeTea) on 1/5/2026.
# This simple script checks for upgrades with Winget. If it detects any, it will run the full upgrade command.
# NOTE: Winget must be installed and properly set up before using. 

# Script header
print("CLI Upgrade Script by Jacob F. (https://www.github.com/FiveEyeTea)")

# Initiates the subprocess module for the run statements. Crucial for running all the winget/choco commands.
from asyncio import subprocess
from subprocess import run

# Initial checks, stored as individual variables.
winget_check = run(["winget", "upgrade"])

# This variable is the upgrade command processes for Winget. It only activates if updates are found.
# NOTE: The "agreements" flags are merely meant for automation. If you don't want the script to automatically accept the agreements, use cli_upgrade_noagree.py instead.
winget_upgrade = run([
    "winget",
    "upgrade",
    "--all",
    "--accept-source-agreements",
    "--accept-package-agreements",
])

# The following print statement is for debugging only: print(winget_check.returncode)

# Checks if the return code is positive. The "agreements" flags are merely meant for automation. If you don't want the script to automatically accept the agreements, use cli_upgrade_noagree.py instead.
if winget_check.returncode == 1:
    run(subprocess.run(winget_upgrade, text=True))
elif winget_check.returncode == 0:
    print("\nNo applicable Winget upgrades found.\n")
else:
    print("ERROR: No return code specified.")
