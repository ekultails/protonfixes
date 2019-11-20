""" Game fix for Space Engineers
"""
#pylint: disable=C0103

import xml.etree.ElementTree as ET
from protonfixes import util

def main():
    """ Installs donet48 and xact. Enables the gcServer.
    """

    # https://github.com/ValveSoftware/Proton/issues/1792#issuecomment-541433879
    util.protontricks('dotnet48')
    util.protontricks('xact')
    config = (util.steamapps_dir() +
              '/common/SpaceEngineers/Bin64/SpaceEngineers.exe.config')
    tree = ET.parse(config)
    root = tree.getroot()

    for element in root.iter('runtime'):
        element.set('gcServer', 'enabled = "true"')

    tree.write(config)
