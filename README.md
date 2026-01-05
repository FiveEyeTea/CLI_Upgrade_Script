# CLI Upgrade Script

A simple Python script which runs both Winget and Chocolatey to check if there are any available updates and, if there are, it re-runs the command to automatically upgrade those packages. Nothing too fancy but can potentially help with maintenance on Windows systems, where automatically updating the bulk of your software can be challenging compared to Linux. Command line package managers like **Winget** and **Chocolatey** offer Linux-like solutions by allowing you to install and update your applications through large software repositories. Scheduling this script to run on a frequent basis could help improve systems' security, particularly for users who want a set-and-forget solution. It could be helpful for setting up on an elderly relative's PC, for example.

## Two versions of the script exist:

### Full

This version is the full script, as I wrote it, which runs both Winget and Chocolatey to check for updates. I use both package managers, but not everyone will have both or want to use both. However, for those who **do** use both, you'll want to download **cli_upgrade_full.py**.

### Winget Only

If you don't have Chocolatey and have no interest in installing it, **cli_upgrade_winget.py** is the version you'll want. It removes the `choco_check` variable and the related `if` statement entirely, running only the `winget_check` variable and subsequent `if` statement.

## Using the script

This is entirely up to you how you use it but if you wanted to automate it, you could run **Task Scheduler** to create a task to run the script on a schedule that you prefer.
