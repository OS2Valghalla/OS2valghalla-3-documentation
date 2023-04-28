# Quick-start installation guide
This guide will covers how to
1. Clone the project
2. Install dependencies
3. Build the project

## 1. Clone the project
Either download the project manuallty or clone using git:
```bash
git clone https://github.com/OS2Valghalla/OS2valghalla-3-documentation.git
```
## 2. Install dependencies
### 2.1 Python
Python 3.10 or newer is required to build the project. Python for Windows, Linux/UNIX, and macOS can be found at [www.python.org/downloads](www.python.org/downloads).
### 2.2 Python packages
The project relies on [pip](https://pip.pypa.io/en/stable/) to install required packages.

In the project environment, run the following command:
```
pip install -r requirements.txt
```
## 3. Build the project
Building the sphinx project creates the documentation HTML files.

To build the project, run the following command in the project environment:
```
$ sphinx-build docs/source docs/source_build/html
```

The documentation HTML output files can be found under [source/_build](docs/source/_build/).