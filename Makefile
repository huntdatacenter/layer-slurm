# TARGETS
lint: clean ## Run linter
	tox -e pep8

clean: ## Remove .tox
	rm -rf .tox/

# Display target comments in 'make help'
help: 
	grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

# SETTINGS
# Silence default command echoing
.SILENT:
# Use one shell for all commands in a target recipe
.ONESHELL:
# Set phony targets
.PHONY: help
# Use bash shell in Make instead of sh 
SHELL=/bin/bash