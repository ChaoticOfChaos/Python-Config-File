##
# Made by ChaoticOfChaos
# Github -> https://github.com/chaoticofchaos
##

# Configuration File Path | Commentary Char for Exclude Commentarys from Variables
def getConfs(configFilePath="./.config.conf", commentary="#")->dict:

    # Refined Content and Config File Contend
    ref_content = []
    configContent = {}

    # Open Configuration File
    with open(configFilePath, 'r') as confiFile:
        content = confiFile.read().split('\n')

    # Verify if Line Exists and If not A Commentary
    for item in content:
        if item and item[0] != commentary:

            # Split Variable Name From Variable Value
            item = item.split('=')
            configContent[item[0]] = item[1]

    return configContent

if __name__ == '__main__':
    # Just a Example
    print(getConfs())