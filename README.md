# CLI Upgrade Script

A simple Python script which runs both Winget and Chocolatey to check if there are any available updates and, if there are, it re-runs the command to automatically upgrade those packages. Nothing too fancy but can potentially help with maintenance on Windows systems, where automatically updating the bulk of your software can be challenging compared to Linux. Command line package managers like **Winget** and **Chocolatey** offer Linux-like solutions by allowing you to install and update your applications through large software repositories. Scheduling this script to run on a frequent basis could help improve systems' security, particularly for users who want a set-and-forget solution. It could be helpful for setting up on an elderly relative's PC, for example.

## Three versions of the script exist:

### Full

This version is the full script, as I wrote it, which runs both Winget and Chocolatey to check for updates. I use both package managers, but not everyone will have both or want to use both. However, for those who **do** use both, you'll want to download **cli_upgrade_full.py**.

### Winget Only

If you don't have Chocolatey and have no interest in installing it, **cli_upgrade_winget.py** is the version you'll want. It removes the `choco_check` variable and the related `if` statement entirely, running only the `winget_check` variable and subsequent `if` statement.

### Winget (No Agree)

This is identical to the Winget Only version except it lacks the two flags to auto agree to package and source agreements. Those flags are included in the other versions to try to better automate the script's process. If you don't mind potentially having to manually agree to these two agreements, and prefer not to be automatically opted in, this is the version of the script to use.

## Using the script

This is entirely up to you how you use it but if you wanted to automate it, you could run **Task Scheduler** to create a task to run the script on a schedule that you prefer.

**Note:** At the time of this commit, you will need to manually run the script as an administrator to use it correctly. If you don't, it likely won't run available updates and if you're using the full version, it will also force you to input a Y/N response to a warning with Chocolatey stating that issues might occur if you go ahead with updates in standard user mode.