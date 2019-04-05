PYTHON3		= python3
VENV		= venv
ACTIVATE	= . ./${VENV}/bin/activate

.PHONY: usage
usage:
	@echo "Usage: ${MAKE} TARGET"
	@echo ""
	@echo "Targets:"
	@echo "  build-env      build venv directory"
	@echo "  clean          remove venv directory"


.PHONY: build-env
build-env: ${VENV}

${VENV}: requirements.txt dev-requirements.txt
	${PYTHON3} -m venv ${VENV}
	${ACTIVATE} && pip install --upgrade pip setuptools wheel
	${ACTIVATE} && pip install --upgrade -r requirements.txt
	${ACTIVATE} && pip install --upgrade -r dev-requirements.txt

requirements.txt:
	touch requirements.txt

dev-requirements.txt:
	echo "flake8" > dev-requirements.txt

.PHONY: clean
clean:
	rm -rf activate ${VENV}
