# Project Makefile for Cryptographic Art Generator

PYTHON=python3
VENV=.venv
ACTIVATE=. $(VENV)/bin/activate;

setup:
	@echo ">>> Creating virtual environment and installing dependencies..."
	$(PYTHON) -m venv $(VENV)
	$(ACTIVATE) pip install --upgrade pip
	$(ACTIVATE) pip install -r requirements.txt
	@echo ">>> Setup complete! Use 'make run' to generate art."

run:
	@echo ">>> Running art generator..."
	$(ACTIVATE) $(PYTHON) -m artgen.cli --text "Hello Makefile" --out output.png
	@echo ">>> Art saved as output.png"

run-text:
	@echo ">>> Running with custom input..."
	$(ACTIVATE) $(PYTHON) -m artgen.cli --text "$(TEXT)" --out "$(OUT)"
	@echo ">>> Art saved as $(OUT)"

test:
	@echo ">>> Running tests..."
	$(ACTIVATE) pytest -q

clean:
	@echo ">>> Cleaning up virtual environment and outputs..."
	rm -rf $(VENV) *.png __pycache__ .pytest_cache
