# Installation

## HyperCells package

```{admonition} Prerequisite
:class: note

GAP version 4.11+
```


First install GAP by following the <a target="_blank" href="https://www.gap-system.org/Download/index.html">instructions</a> on the GAP website. In most cases, this boils down to the following steps (to be executed in the directory where GAP should be installed to):
```shell
sudo apt-get install build-essential autoconf libtool libgmp-dev libreadline-dev zlib1g-dev
wget https://github.com/gap-system/gap/releases/download/v4.12.2/gap-4.12.2.tar.gz
tar -zxf gap-4.12.2.tar.gz
cd gap-4.12.2/
./configure
make
cd pkg
../bin/BuildPackages.sh
cd ..
```
You might want to link the executable to `~/bin/gap`:
```shell
ln -s gap-4.12.2/gap ~/bin/gap
```
and add `~/bin/` to your path if you have not done so yet:
```shell
echo "export PATH=\"$PATH:~/bin\"" >> ~/.bashrc
```

The HyperCells package is most easily installed by simply cloning the git repository in the user's GAP package directory:
```shell
mkdir -p ~/.gap/pkg
cd ~/.gap/pkg
git clone https://github.com/patrick-lenggenhager/HyperCells.git
```
To update it to the most recent version, simply pull:
```shell
cd ~/.gap/pkg/HyperCells
git pull
```


## HyperBloch package

```{admonition} Prerequisites/Dependencies
:class: note

- Wolfram Language Interpreter such as <a target="_blank" href="https://www.wolfram.com/engine">Wolfram Language Engine</a>
or <a target="_blank" href="https://www.wolfram.com/mathematica">Mathematica</a> with Wolfram Language 12+ (13+ is recommended) 
- <a target="_blank" href="https://github.com/NCAlgebra/NC">NCAlgebra</a> package (version 6+)
```

Assuming a Wolfram Language Interpreter is already installed, we first install its dependency NCAlgebra
```Mathematica
PacletInstall["https://github.com/NCAlgebra/NC/blob/master/NCAlgebra-6.0.3.paclet?raw=true"];
```
and then the package itself as a paclet:
```Mathematica
PacletInstall["https://github.com/patrick-lenggenhager/HyperBloch/releases/download/v0.9.0/PatrickMLenggenhager__HyperBloch-0.9.0.paclet"]
```
If necessary, update the version number to match the one of the <a target="_blank" href="https://github.com/patrick-lenggenhager/HyperBloch/releases/latest">latest release</a>. Alternatively, download the release file manually, and install it with <code class="language-Mathematica">PacletInstall["path"]</code> by passing the path to the downloaded file as argument.
