# ===============================================================================================
# Inter-link featured functions in the getSetGo files and tutorials:
# ===============================================================================================
# If you want to disable the execution of this code section, please make sure to delete the code:
# .. include:: interlinkTutorials.rst
#   :start-line: 2
# which is part of the contents/Tutorials/tutorials.rst file.
# ===============================================================================================
# Import packages and modules:
# ===============================================================================================

import sys, os

sys.path.append(os.path.abspath(''))
from interlink import pageffsDict, ffspageDict, interlinkFile, mergeDicts

# ===============================================================================================
# Preliminaries:
# ===============================================================================================

# set up path
cwd = os.getcwd() # current directory
dirTutorials = "/contents/Tutorials/" # relative path to the tutorials
dirGetSetGo = "/contents/GettingStarted/" # relative path to the getSetGo files

# list of excluded files
exclude_files_tutorials = [
    "tutorials.rst",
    "AdvancedVisualization.md",
    "interlinkTutorials.rst"
]

# list of excluded files
exclude_files_getSetGo = [
    "getting_started.rst"
]

# extract list of available files
filesTutorials = [f for f in os.listdir(cwd + dirTutorials) 
        if os.path.isfile(os.path.join(cwd + dirTutorials, f))
        and f not in exclude_files_tutorials ]


filesGetSetGo = [f for f in os.listdir(cwd + dirGetSetGo) 
        if os.path.isfile(os.path.join(cwd + dirGetSetGo, f))
        and f not in exclude_files_getSetGo ]

# ===============================================================================================
# Start inter-linking:
# ===============================================================================================

# get dicts of the form {package1 : {page1 : featured function list1, ... }, ...} and .rst hyperlinks
[pffsDicsTutorials, rstLinksTutorials] = pageffsDict(cwd + dirTutorials, filesTutorials, rstLinks=True)
[pffsDicsGetSetGo, rstLinksGetSetGo] = pageffsDict(cwd + dirGetSetGo, filesGetSetGo, rstLinks=True, dirLink="../GettingStarted/", refName="Getting started - ")

# merge dictionaries
pffsDics = {
    "HyperCells" : 
        mergeDicts(pffsDicsTutorials["HyperCells"], pffsDicsGetSetGo["HyperCells"]), 
    "HyperBloch" :
        mergeDicts(pffsDicsTutorials["HyperBloch"], pffsDicsGetSetGo["HyperBloch"])
}

# convert dicts to the form {package1 : {featured function1 : page list1 , ... }, ...}
[ffspDics, rstLinks] = ffspageDict("", [], rstLinks = True, preDic = [pffsDics, rstLinksTutorials + rstLinksGetSetGo])

# generate .rst file
interlinkFile(cwd + dirTutorials, "interlinkTutorials", ffspDics, rstLinks=rstLinks)
# ===============================================================================================