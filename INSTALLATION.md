# Quick-start installation guide
This guide will cover how to
1. Clone the project
2. Install dependencies
3. Build the project

## 1. Clone the project
Either download the project manually or clone using git:
```bash
git clone https://github.com/OS2Valghalla/OS2valghalla-3-documentation.git
```
## 2. Install dependencies
### 2.1 Python
Python 3.10 or newer is required to build the project. 

Python for Windows, Linux/UNIX, and macOS can be found at [www.python.org/downloads](https://www.python.org/downloads/).

Make sure Python is available in PATH.
### 2.2 Python packages
The project relies on [pip](https://pip.pypa.io/en/stable/) to install required packages. **pip** comes pre-installed with Python 3.4 and newer.

In the project environment, run the following command:
```
pip install -r requirements.txt
```
## 3. Build the project
Building the Sphinx project creates the documentation HTML files.

To build the project, run the following command in the project environment:
```
sphinx-build docs/source docs/source/_build/html
```

The documentation HTML output files can be found under [source/_build](docs/source/_build/).

> :warning: It is important that the selected Python interpreter is the same as where the required Python packages are installed. This is true whether the Python packages are installed globally or only in the virtual environment. See *[Manually specify an interpreter](https://code.visualstudio.com/docs/python/environments#_manually-specify-an-interpreter)* for more information.

See the [Recommended extensions](SPHINXGUIDE.md#5-recommended-extensions) section of the [Quick-start Sphinx and reStructuredText guide](SPHINXGUIDE.md) for extensions that can greatly improve the editor experience, such as auto-building and live previews.
