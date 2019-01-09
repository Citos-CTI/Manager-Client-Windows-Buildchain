import os
import wget
from github3 import login


token = 'a0c2a8015a5c71a0947ba5e6805ef0a97cd3805d'
gh = login('','',token)

string_upl = ""
import requests
sessionObj = requests.session()
url1='https://api.github.com/user'
r = requests.get('https://api.github.com/user', auth=('Johnny-Engler', 'a0c2a8015a5c71a0947ba5e6805ef0a97cd3805d'))

with requests.get('https://api.github.com/repos/Citos-CTI/Client/releases/latest') as response:
    data = response.json()
    for str in data['assets']:
        if str['name'].startswith('citos') and str['name'].endswith('.jar'):
            splitted = data['html_url'].split('/')

            with open('version.txt', 'r') as input:
                if input.readline().startswith(splitted[-1]):
                    print('No new version found, exiting...')
                    break
            print('New version found, downloading .jar...')
            if os.path.isfile('version.txt'):
                os.remove('version.txt')
            if os.path.isfile('Citos.jar'):
                os.remove('Citos.jar')
            with open('version.txt', 'a') as out:
                out.write( splitted[-1]+ '\n')

            wget.download(str['browser_download_url'], 'Citos.jar')

            from subprocess import call
            call(["sh", "buildInstaller.sh"])

            print("Installer generated, uploading installer...")

            file = open("installer/Citos_Installer.exe", "rb")
            gh.repository(owner="Citos-CTI", repository="Client").latest_release().upload_asset("application/octet-stream",name="Citos_Installer.exe", asset=file)

            print("upload finished")
            input = open("version.txt", "r")

