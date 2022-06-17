# Python CLI

This CLI template doesn't do very much, it just prints out text, but you can fill in the blanks and add to it to build a real CLI.

![example-commmands](./docs/example-commands.jpg)
<br>
<br>

## Running Commands

For testing the commands you build, you can call them like this. This will save you rebuilding the WHL file each time to to test something.

### Bash
```bash
python3 -m python_cli:main <args>
python3 -m python_cli:main start -n server1 -m "start reason"
```

### Windows
```
python -m python_cli:main <args>
python -m python_cli:main start -n server1 -m "start reason"
```
<br>
<br>


## Build And Install The WHL

You can build the CLI into a WHL file and install it to be called from anywhere on your system.

Building will require you to have setuptools and wheel isntalled.

```bash
make build
make install
```

Once the WHL is installed you can call it directly from your CLI
(terminal or powershell)

```bash
python_cli start -n server1 -m "starting server to spend money"
python_cli stop -n server2 -m "stopping server to save money"
```
<br>
<br>


## List Of Commands
```
python_cli create server -u "FoodyFood"
python_cli create bucket -n "bucket-123"

python_cli start -n "server1" -m "I started this to spend money"
python_cli stop -n "server2" -m "I stopped this to save money"

python_cli delete server -u "FoodyFood"
python_cli delete bucket -n "bucket-456" -u "FoodyFood"
```
<br>
<br>



