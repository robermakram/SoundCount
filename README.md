# SoundCount

Install the python package manager PIP
python<3> get-pip.py or sudo easy_install pip

Most system use Python 2.7 as the default python interpreter. Be sure to check which python you're using with python --version if you are unsure of your system's default python interpreter. You more than likely need to use python3. Pip might be available via brew for macOS: brew install pip3 will likely work. I also think there maybe a way to get pip via packages such as sudo apt install python3-pip in most Ubuntu/apt based systems. You may also use pip --version to display which python pip will use.

Install virutalenv
install virtualenv using pip:

pip<3> install virtualenv

virtualenv is used to create and manage environments for different python projects. Use virtualenv to create a virtual environment by using:

virtualenv env

NOTE: If you are in a virtual environment -- do not, EVER, use sudo, as this will not install into the virutal environment. In a virtual environment, the packages are installed in (this case) to the folder env

Switching environments
Use source env/bin/activate to load your environment. env is a placeholder for your environment name.

use deactivate to exit out of your environment.

To verify which environment you're in, use which pip. if you see that the pip location is in your environment folder (env), then you are in your virtual environment. Also notice that in virtualenv, python3 is now the default interpreter which makes life much easier. Check using python --version and notice the lack of 3 at the end.

Then install python packages by:
pip install -r requirements.txt
