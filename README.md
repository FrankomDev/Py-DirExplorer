# Python DirExplorer

Python web directory/subdomain finder -- something like dirbuster

## Usage
``git clone https://github.com/FrankomDev/Py-DirExplorer.git`` <br>
``cd Py-DirExplorer/`` <br>
``pip install -r requirements.txt`` <br>
``python3 direxplorer.py -h``

or with venv:

``python3 -m venv venv`` <br>
``./venv/bin/pip install -r requirements.txt`` <br>
``./venv/bin/python3 direxplorer.py -h``

## Example
``python3 direxplorer.py -u https://frankom.top -w wordlist.txt -a dns``