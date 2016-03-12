#!/usr/bin/python

import subprocess


def runShellCommand(command):
    # Assign the command to process.
    process = subprocess.Popen(
        command.split(), stdout=subprocess.PIPE)
    # Run the command and return the output
    output = process.communicate()[0]
    return output


def runShellScript(script):
    # Read the file and close it when done
    with open(script, 'r') as scriptFile:
        commands = scriptFile.read().replace('\n', '')
        return runShellCommand(commands)
