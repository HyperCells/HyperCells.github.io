# The HyperCells & HyperBloch website

This website serves as a comprehensive guide to the installation and usage of the
[HyperCells](https://github.com/HyperCells/HyperCells) and
[HyperBloch](https://github.com/HyperCells/HyperBloch) packages, providing tutorials with
detailed explanations ranging from simple examples to more advanced applications.

The website is online here: [https://hypercells.github.io/](https://hypercells.github.io/).

#### Table of contents
  - [Authors](#authors)
  - [Building and viewing the website](#building-and-viewing-the-website)
  - [Contact](#contact)
  - [License and copyright](#license-and-copyright)

## Authors

Main author and developer:\
&ensp;&ensp;**Marcelo Looser**

Coauthors:\
&ensp;&ensp;**Patrick M. Lenggenhager** ([https://patrick-lenggenhager.github.io](https://patrick-lenggenhager.github.io), plengg@pks.mpg.de)\
&ensp;&ensp;**Tomáš Bzdušek** (tomas.bzdusek@uzh.ch)

## Building and viewing the website

1. Install [Python](https://www.python.org/).
2. Set up the environment, e.g., using `venv`:
```bash
python -m venv env
source env/bin/activate
pip install --upgrade pip
```
3. Install the necessary Python packages
```bash
pip install -r requirements.txt
```
4. Install [make](https://www.gnu.org/software/make/).
5. Build HTML
```bash
make html
```
6. Start a webserver in the directory `build/html`, e.g., in VSCode use the [LiveServer](https://marketplace.visualstudio.com/items?itemName=ritwickdey.LiveServer) extension.

## Contact

To report issues, please use the issue tracker at
[https://github.com/HyperCells/HyperCells.github.io/issues](https://github.com/HyperCells/HyperCells.github.io/issues).

## License and copyright

See the attached [LICENSE](LICENSE.txt) for details.

&copy; 2024 Marcelo Looser, Patrick M. Lenggenhager, Tomáš Bzdušek