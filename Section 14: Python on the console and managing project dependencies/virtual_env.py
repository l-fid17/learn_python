# create virtual env with name "venv" using python 3 by default
virtualenv venv --python=python3

# activate the venv from project folder (use path to activate file inside venv folder)
source venv/activate

# de-activate venv
deactivate

# install packages with (replace package with package name)
pip install package

# show versions of installed dependencies
pip freeze

# save dependencies and versions list to file
pip freeze > requirements.txt

# install dependencies from file
pip install -r requirements.txt