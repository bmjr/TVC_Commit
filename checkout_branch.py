import re
import shell_engine


def getBranchName(cardTitle):
    brackets = re.search('\[([A-Za-z0-9_]+)\]',cardTitle)
    if brackets:
        branchName = brackets.group(1)

        # Test the output of this function
        return branchName


def createBranch(branchName):
    checkoutBranch = "git checkout -b " + branchName
    shell_engine.runShellCommand(checkoutBranch)
    shell_engine.runShellCommand("git push origin " + branchName)
