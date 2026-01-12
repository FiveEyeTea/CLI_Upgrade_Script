# CLI Upgrade Script
# Initially written by Jacob F. (https://www.github.com/FiveEyeTea) on 1/5/2026
# This simple script checks for upgrades with Winget. If it detects any, it will run the full upgrade command.
# Winget must be installed and properly set up before using. This variant removes the auto-agree flags but may require more input.

# Script header
print("CLI Upgrade Script by Jacob F. (https://www.github.com/FiveEyeTea)")

# Initiates the subprocess module for the run statements. Crucial for running all the winget/choco commands.
from asyncio import subprocess
from subprocess import run

# Initial checks, stored as individual variables.
winget_check = run(["winget", "upgrade"])

# This variable is the upgrade command processes for Winget. It only activates if updates are found.
# NOTE: Without the agreements flags, from the main script, users may be prompted to accept agreements during upgrade.
winget_upgrade = run([
    "winget",
    "upgrade",
    "--all",
])

# The following print statement is for debugging only: print(winget_check.returncode)

# Checks if the return code is positive.
if winget_check.returncode == 1:
    run(subprocess.run(winget_upgrade, text=True))
elif winget_check.returncode == 0:
    print("\nNo applicable Winget upgrades found.\n")
else:
    print("ERROR: No return code specified.")
