#usr /bin/bash/python3
import os
try:
    if (os.getuid() == 0):
        print("Starting Firefox Developer Edition Installation")
        os.system("cp default128.png firefox/icons/")
        os.system("cp -r firefox/ /opt/")
        print("Installed Firefox Developer Edition")
        print("Create Shorcut Desktop")
        os.system("cp firefox-developer.desktop /usr/share/applications/")
        print("Sucsessful Installation")
        print("#### Thanks for using. #Tayentu -- Github:enestunclar")
    else:
        print("You are not Root. Please run command sudo.")
except:
    print("Error. Exiting Installation. Please read error code.")

