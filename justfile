build:
  @git pull
  @pip install --upgrade pip
  @python -m pip install -r requirements.txt --upgrade
  @python -m pip install .

pypi:
  @git pull
  @pip install --upgrade pip
  @rm dist/* && python -m build
  @twine upload dist/*
  @python -m pip install -r requirements.txt --upgrade
  @python -m pip install .