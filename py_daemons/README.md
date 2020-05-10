# Python Daemon Template Code

## Summary
- App summary

## Usage
The code works as a daemon. You can manage it like most services in Linux:

- Starting: ```sudo python3 <path to obfuscator.py> start```
- Stopping: ```sudo python3 <path to obfuscator.py> stop```
- Status: ```sudo python3 <path to obfuscator.py> status```

## Install Dependencies
- Debian Linux: ```sudo apt-get install python3-dev```
- RHEL Linux: ```sudo yum install python3x-dev```
    - E.g. if you are running python 3.6, then ```sudo yum install python36-dev```
- ```sudo -H python3 -m pip install service```
- NOTE: you may need to install GCC