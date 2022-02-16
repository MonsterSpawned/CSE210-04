# Install Python 3 VirtualEnv dependencies, whilst creating a Virtual Evnvironment called "venv."
sudo apt install -y python3-pip
python3 -m pip install virtualenv
virtualenv ./venv

# Activate the VENV:
source ./venv/bin/activate
sudo apt install python3-tk
sudo python3 -m pip install -r ./requirements.txt