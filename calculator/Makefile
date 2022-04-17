VENV = env
PYTHON = $(VENV)/bin/python
PIP = $(VENV)/bin/pip
APP = calculator.py

run: $(VENV)/bin/activate
	$(PYTHON) $(APP)


$(VENV)/bin/activate: requirements.txt
	python3.10 -m venv $(VENV)
	$(PIP) install -r requirements.txt


clean:
	rm -rf $(VENV)run: env/bin/activate