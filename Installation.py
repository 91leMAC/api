# Using camelCase bcs I like it more.
import os
import subprocess
# Please install pyton3 using this command: sudo apt install python3
# Run this script as root run this command: su
# Aiming at least to use just one time "os.system()" method. 

# BIG WARNING never tested please delete me after the test.
installation = "apt install pip -y && pip install geopy -y & apt install certbot python3-certbot-nginx"

gitInstallation = "apt install git -y"
verifyGitInstallation = os.system(gitInstallation)
if gitVerify == 0:
    print("error: Git run into an issue to install, please install it manually using: $ sudo apt install git")
    else:
    print("Git succesfully installed!")

getAPI = "cd && git clone https://github.com/Ccccccc667jjj/api.git"
goAndRunAPI = "cd api && nohup python3 api.py & && chmod +x api.py && ufw allow 5000"

getUserDomain = input("Please insert your domain name like: google.com \n")

SPsiteCreationFolder = ["mkdir", f"/var/www/{getUserDomain}"]
SPsiteGoFolder = ["cd", f"/var/www/{getUserDomain}"]
importingGitSite = "git clone https://github.com/Ccccccc667jjj/site"
SPrenameFile = ["rm", "domain.conf", f"{getUserDomain}.conf"]
SPcertbot = ["certbot", "certonly", "--nginx", "d", f"{getUserDomain}.conf"]
restartNginx = "systemctl restart nginx"

os.system(installation)
os.system(getAPI)
os.system(goAndRunAPI)
subprocess.run(SPsiteCreationFolder)
subprocess.run(SPsiteGoFolder)
os.system(importingGitSite)
subprocess.run(SPrenameFile)
subprocess.run(SPcertbot)
os.system(restartNginx)



