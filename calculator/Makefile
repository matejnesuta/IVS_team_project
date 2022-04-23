VENV = env
PYTHON = $(VENV)/bin/python
PIP = $(VENV)/bin/pip
APP = calculator.py

.DEFAULT_GOAL = all

all:
	@echo "all"

pack:
	@echo "pack"

test:
	@echo "test"

doc:
	@echo "doc"

profile:
	@echo "profile"

help:
	@echo "---------------HELP-----------------"
	@echo "all (přeloží projekt - včetně programu pro profiling)"
	@echo "pack (zabalí projekt tak, aby mohl být odevzdán)"
	@echo "clean (smaže všechny soubory, co nemají být odevzdány)"
	@echo "test (spustí testy matematické knihovny)"
	@echo "doc (spustí generování dokumentace)"
	@echo "run (spustí program)"
	@echo "profile (spustí překlad programu pro výpočet směrodatné odchylky na profiling)"
	@echo "Při spuštění make bez uvedení cíle se provede make all."

run: $(VENV)/bin/activate
	$(PYTHON) $(APP)


$(VENV)/bin/activate: requirements.txt
	python3.10 -m venv $(VENV)
	$(PIP) install -r requirements.txt


clean:
	rm -rf $(VENV)