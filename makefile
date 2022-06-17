# Some shortcuts to test various commands


# Create infra
create-server:
	@python3 -m python_cli.main create server -u "FoodyFood"
create-bucket:
	@python3 -m python_cli.main create bucket -n "bucket-123"



# Delete infra
delete-server:
	@python3 -m python_cli.main delete server -u "FoodyFood"
delete-bucket:
	@python3 -m python_cli.main delete bucket -n "bucket-456" -u "FoodyFood"



# Affect current infra
start:
	@python3 -m python_cli.main start -n "server1" -m "I started this to spend money"
stop:
	@python3 -m python_cli.main stop -n "server2" -m "I stopped this to save money"



# Test no user input
none:
	@python3 -m python_cli.main



# Display the help message
help:
	@python3 -m python_cli.main --help



# Build the WHL
.PHONY: build
build:
	rm -rf build *.egg-info
	python3 setup.py bdist_wheel



# Install/Uninstall The CLI
install:
	pip3 install ./dist/python_cli-1.0-py3-none-any.whl

uninstall:
	pip3 uninstall -y python_cli



# Time Saver; build, uninstall old build, install new build
rebuildinstall: build uninstall install

