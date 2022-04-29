VENV = env
PYTHON = $(VENV)/bin/python
PIP = $(VENV)/bin/pip
APP = calculator.py
PROFILER = profiling.py
DATA = data.txt
.DEFAULT_GOAL = all
DOXYFILE = Doxyfile
LATEX_CMD = pdflatex
XLOGINS = xnesut00_xpenko00_xdzida01_xmarke00

 .PHONY: all pack packfolder test doc profile help run clean

all: $(VENV)/bin/activate

pack: clean doc packfolder ../../$(XLOGINS).zip

../../$(XLOGINS).zip:
	rm -rf ../installer
	rm -rf ../doc	
	cd ../.. && zip -r $@ $(XLOGINS) 
	
packfolder:
	mkdir -p ../../$(XLOGINS)/repo
	mkdir -p ../../$(XLOGINS)/installer
	mkdir -p ../../$(XLOGINS)/doc
	cp -af ../../repo/. ../../$(XLOGINS)/repo/
	cp -af ../doc/. ../../$(XLOGINS)/doc/
	cp -af ../installer/. ../../$(XLOGINS)/installer/

test: $(VENV)/bin/activate
	$(PYTHON) -m pytest

doc: $(DOXYFILE)
	doxygen $(DOXYFILE)	
	cd ../doc/latex/ ; make -i pdf
	
	mv ../doc/latex/refman.pdf ../doc/dokumentace.pdf 
	rm -rf ../doc/latex

profile: $(VENV)/bin/activate
	$(PYTHON) $(PROFILER) < $(DATA)
	$(PYTHON) $(VENV)/lib/python3.10/site-packages/gprof2dot.py -f pstats profiling_calc.prof | dot -Tpng -o output.png
	mv output.png ../profiling/vystup.png

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
	rm -f *.prof
	rm -rf mathlib/__pycache__
	rm -rf __pycache__
	rm -rf *.log
	rm -rf .pytest_cache