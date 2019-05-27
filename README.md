# GoCD Encrypt Script written in Python

A simple script that takes some files from stdin and encrypts them against the GoCD API to return a gocd variable

**General process:**

+ curl a payload against the API using user credentials
+ Take note ofthe returned encrypted value
+ Use the returned value within your pipeline as code

Given a file or string, encrypt a variable with a certain GoCD instance. Returns an encrypted base64 string to input into pipelines-as-code.

**Installation:**

We use a number of modules with this script so it's likely best to use the requirements.txt to install everything within a virtual env:

```
$ virtualenv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

**Usage:**

```
# To encrypt a string:
python encrypt_variables.py --username <password> --password <password> --hostname <gocd server> --data <string>

# To encrypt a file:
python encrypt_variables.py --username <username> --password <password> --hostname <gocd server> --mode file --data <filename>
```

## Contributing:

Python 2.7, use a virtualenv!

```
$ virtualenv venv
```

Conform to PEP8 standards, and lint against that.

## TODO:
* Get this in a pipeline to stop pesky non-conforming commits occuring (CI)
* Allow config file (CI)
* Add support for directories, and writing of 'enrypted' files into a specific directory (Improvements)
* Add new 'prompt' parameter to allow password input (Improvements)
+ Migrate to user input not variables
+ Addition of cclick library to make it more native

