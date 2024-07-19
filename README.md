# The HyperCells & HyperBloch website

This website demonstrates the usage of the HyperCells and HyperBloch packages through
examples, guides, and tutorials.

## Building and Viewing the Website

1. Install [Python](https://www.python.org/).
2. Set up the environment, e.g., using `venv`:
```bash
python -m venv env
source env/bin/activate
pip install --upgrade pip
```
3. Install the necessary Python packages
```bash
pip install -r requirements_pip.txt
```
4. Install [make](https://www.gnu.org/software/make/).
5. Build HTML
```bash
make html
```
6. Start a webserver in the directory `build/html`, e.g., in VSCode use the [LiveServer](https://marketplace.visualstudio.com/items?itemName=ritwickdey.LiveServer) extension.