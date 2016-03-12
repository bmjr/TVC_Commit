import re
import shell_engine


def getBranchName(cardTitle):
    m = re.search('(?:\[)+.+(?:\])', cardTitle)
    if m:
        branchName = m.group(1)
        # Test the output of this function
        return branchName


def createBranch(branchName):
    checkoutBranch = "git checkout -b " + branchName
    shell_engine.runShellCommand(checkoutBranch)
