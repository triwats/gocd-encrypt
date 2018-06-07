# BookingGo GoCD Scripts

Numerous scripts for interacting and working with GoCD

**Python:**
All conforming to PEP8 standards

`encrypt_variables.py:`

Given a file or string, encrypt a variable with a certain GoCD instance. Returns an encrypted base64 string to input into pipelines-as-code. 

Installation:

We use a number of modules with this script so it's likely best to use the requirements.txt to install everything within a virtual env:

```
$ virtualenv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

Usage:

```
python encrypt_variables.py --username <password> --password <password> --hostname <gocd server> --data <string>
python encrypt_variables.py --username <username> --password <password> --hostname <gocd server> --mode file --data <filename>
```

## Development:

To develop against this in Python you should be using a virtual env of some description at all times:

```
$ virtualenv venv
```

Conform to PEP8 standards, and lint against that.

## TODO: 
Get this in a pipeline to stop pesky non-conforming commits occuring 

