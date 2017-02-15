VENV=./venv
PYTHON=$(VENV)/bin/python
PIP=$(VENV)/bin/pip

$(VENV):
	pyvenv $(VENV)
	$(PIP) install -U pip

depends: $(VENV)
	$(PIP) install circus PyYAML


run: depends
	$(PYTHON) ./vpn_watchdog/woof.py
