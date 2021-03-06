export CFLAGS=-Qunused-arguments
export CPPFLAGS=-Qunused-arguments

CWD="`pwd`"
PROJECT_NAME = venus
PROJECT_HOME ?= $(CWD)
PROJECT_CODE =$(PROJECT_HOME)/src
PROJECT_TEST =$(PROJECT_HOME)/tests
NEW_PYTHONPATH=$(PROJECT_CODE):$(PYTHONPATH)


clean:
	@echo "Cleaning up *.pyc files"
	@find . -name "*.pyc" -delete


setup:
	@echo "Installing dependencies..."
	@pip install -r $(PROJECT_HOME)/requirements.txt
	@pip install -r $(PROJECT_HOME)/requirements_test.txt
	@echo "Adding git hooks..."
	@cp ./helpers/git-hooks/pre-commit ./.git/hooks/pre-commit
	@chmod ug+x ./.git/hooks/pre-commit

pep8:
	@echo "Checking source-code PEP8 compliance"
	@-pep8 $(PROJECT_CODE) --ignore=E501,E126,E127,E128

pep8_tests:
	@echo "Checking tests code PEP8 compliance"
	@-pep8 $(PROJECT_TEST) --ignore=E501,E126,E127,E128

lint:
	@echo "Running pylint"
	@pylint $(PROJECT_CODE)/$(PROJECT_NAME) --disable=C0301 --disable=C0103

unit: clean pep8 pep8_tests
	@echo "Running pep8 and unit tests..."
	@nosetests -s  --cover-branches --cover-erase --with-coverage --cover-inclusive --cover-package=$(PROJECT_NAME) --tests=$(PROJECT_TEST)/unit --with-xunit

integration: clean pep8 pep8_tests
	@echo "Running pep8 and integration tests..."
	@nosetests -s  --cover-branches --cover-erase --with-coverage --cover-inclusive --cover-package=$(PROJECT_NAME) --tests=$(PROJECT_TEST)/integration --with-xunit

tests: clean pep8 pep8_tests lint
	@echo "Running pep8, lint, unit and integration tests..."
	@nosetests -s  --cover-branches --cover-erase --with-coverage --cover-inclusive --cover-package=$(PROJECT_NAME) --tests=$(PROJECT_TEST) --with-xunit

run:
	@cd src; PYTHONPATH=`pwd`:$PYTHONPATH python -m venus.main 
