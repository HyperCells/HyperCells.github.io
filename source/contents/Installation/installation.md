
<style type="text/css">
    @media (min-width: 959.98px) {
        .bd-main .bd-content  {
            max-width: 84.1%;  
            align-self: end;
            }
        .bd-main .bd-content .bd-sidebar-secondary .bd-toc {
            align-items:right;
            }
</style>



# Installation

## HyperCells package

```{admonition} Prerequisite
:class: note

GAP version 4.11+
```

First install GAP by following the <a target="_blank" href="https://www.gap-system.org/Download/index.html">instructions</a> on the GAP website. In most cases, this boils down to the following steps which installs GAP 4.12.2 (to be executed in the directory where GAP should be installed to):
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
git clone https://github.com/HyperCells/HyperCells.git
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

```{admonition}  NCAlgebra
:class: danger

* All NCAlgebra paclet versions smaller than version 6 are incompatible. 
* We recommend to install the paclet via the function <code class="code-Mathematica">PacletInstall</code> as described below.
* Otherwise, if a problem occurs during a manual installation, please follow the instructions below, instead.
```

Assuming a Wolfram Language Interpreter is already installed, we first install its dependency NCAlgebra
```Mathematica
PacletInstall["https://github.com/NCAlgebra/NC/blob/master/NCAlgebra-6.0.3.paclet?raw=true"];
```

and then the package itself as a paclet:
```Mathematica
PacletInstall["https://github.com/HyperCells/HyperBloch/releases/download/v1.0.0/PatrickMLenggenhager__HyperBloch-1.0.0.paclet"]
```
If necessary, update the version number to match the one of the <a target="_blank" href="https://github.com/HyperCells/HyperBloch/releases/latest">latest release</a>. Alternatively, download the release file manually, and install it with <code class="code-Mathematica">PacletInstall["path"]</code> by passing the path to the downloaded file as argument.


## Extensions (optional)

The HyperCells package has an integrated word simplification procedure for a selection of functions. Two methods are available: a default brute-force method, and a method based on the Knuth-Bendix completion algorithm. The latter can only be used provided the <a target="_blank" href="https://gap-packages.github.io/kbmag/doc/chap0_mj.html">kbmag</a> package (version 1.5.10+) is available. 

The default configuration of the kbmag package allows HyperCells to simplify words in groups with a maximal number of generators of 127. However, this limit can manually be extended up to 65535. The corresponding adjustments are laid out in a README file in the kbmag package and can be found in the folder containing GAP: “…/gap/gap-< version >/pkg/kbmag/standalone”, with the following instructions:

```
NEW in Version 2.3: It is now possible to use kbmag with more than the
previous default number of 127 generators. To use up to 65535 generators,
before making the package, edit the file "defs.h" in the lib directory,
and change the two lines:

#define MAXGEN MAXCHAR /* maximum number of generators */
typedef char gen; /* for generators of monoids and groups */

to

#define MAXGEN MAXUSHORT /* maximum number of generators */
typedef unsigned short gen; /* for generators of monoids and groups */
```

Once these changes are made, kbmag needs to be recompiled. This can be done in the terminal, where in the kbmag directory one needs to execute the command **make clean** and afterwards **make**.

If these changes are not made while using the Knuth-Bendix completion algorithm based simplification and unit cells compactified on Riemann surfaces with genus exceeding 63 are used, the procedure will not be executed and a warning will be printed in GAP:

<div class="highlight-gap notranslate"><div class="highlight">
<pre><span></span><span class="c1">#WARNING: maximal number of generators have been exceeded; non-simplified words will 
be used. Please follow the instructions in the chapter Introduction section Simplify
extension (optional) in the HyperCells reference manual.</span>
</pre></div>
</div>
