# ===============================================================================================
# HyperCells-website: interlinking getSetGo files & tutorials (etc.):
# ===============================================================================================
# This script is intended to construct an additional .rst file in the GettingStarted & tutorials
# directory in order to interlink the featured functions and with the getSetGo and the tutorials, 
# as such, certain critical assumptions are made. The script will be executed within the conf.py 
# file, which creates the rst files during the build, and will be embedded in the 
# getting_started.html and tutorials.html files. However, in principle, (probably minor) modifi-
# cations can be made for other interlinking purposes if they are needed.
# ===============================================================================================
# Import packages :
# ===============================================================================================

import re

# ===============================================================================================
# Helper functions  :
# ===============================================================================================

def pageTitle(mdStr):
    """ Extract the page title.

    Parameters
    ----------
    mdStr : string
        String of a markdown file.

    Returns
    -------
    A string with the first substring between characters #  and \n,
    which is assumed to be the page title.
    """
    return mdStr.split("# ")[1].split("\n")[0]


def featuredFuncs(mdStr):
    """ Extract all featured functions.

    Parameters
    ----------
    mdStr : string
        String of a markdown file.

    Returns
    -------
    A string with the first substring between characters ....Featured function ... and ...\n```,
    which is assumed to be a string containing all featured functions
    """
    return mdStr.split("```{dropdown}  Featured functions\n:color: info\n:icon: gear")[1].split("</code>\n```")[0] + "</code>"


def HCfeaturedFuncs(ffsStr):
    """ Extract the HyperCells featured functions.

    Parameters
    ----------
    ffsStr : string
        Featured function strings.

    Returns
    -------
    A string with the first substring between characters '<code class="code-gap">' and </code>,
    which is assumed to be a string congaing featured functions of the HyperCells package.
    """
    HCffsStr = ffsStr.split('<code class="code-gap">')[1].split("</code>")[0]
    HCffs = [re.sub("\n", "", re.sub(" ", "", func)) for func in HCffsStr.split(",")]
    return HCffs


def HBfeaturedFuncs(ffsStr):
    """ Extract the HyperBloch featured functions.

    Parameters
    ----------
    ffsStr : string
        Featured function strings.

    Returns
    -------
    A string with the first substring between characters '<code class="code-Mathematica">' and </code>,
    which is assumed to be a string congaing featured functions of the HyperBloch package.
    """    
    HBffsStr = ffsStr.split('<code class="code-Mathematica">')[1].split("</code>")[0]
    HBffs = [re.sub("\n", "", re.sub(" ", "", func)) for func in HBffsStr.split(",")]
    return HBffs

 
def pageffsDict(path, fileNames, rstLinks = False):
    """ Construct two dictionaries of featured functions.

    Parameters
    ----------
    path : string
        Absolute path to the markdown files.
    fileNames : string
        File names of the markdown files.
    rstLinks : boolean, optional
        Whether to return a list .rst hyperlinks. The default is False.

    Returns
    -------
    pffsDics : dictionary
        A dictionary of two dictionaries with page titles of the files as keys and a list
        of all featured functions as values, HyperCells and HyperBloch, respectively.
    """
    hyLinks = []   
    pffsHCDic, pffsHBDic = {}, {}
    for file in fileNames:
        f =  open(path + file, 'r')
        mdStr = f.read()
        ffsStr = featuredFuncs(mdStr)

        title = pageTitle(mdStr)
        if rstLinks:
            hyLinks.append(f'.. _{title}: ./{file[:-3]}.html')
        title = "`" + title + "`_"

        ffsLst = []
        if '<code class="code-gap">' in ffsStr:
            ffsLst = ffsLst + HCfeaturedFuncs(ffsStr)
            pffsHCDic[title] = ffsLst

        ffsLst = []
        if '<code class="code-Mathematica">' in ffsStr:
            ffsLst = ffsLst + HBfeaturedFuncs(ffsStr)
            pffsHBDic[title] = ffsLst
    
    pffsDics = {"HyperCells" : pffsHCDic, "HyperBloch" : pffsHBDic}
    if rstLinks:
        return [pffsDics, hyLinks]
    else:
        return pffsDics


def ffspageDict(path, fileNames, rstLinks = False, preDic = None):
    """ Construct two dictionaries of featured functions.

    Parameters
    ----------
    path : string
        Absolute path to the markdown files.
    fileNames : string
        File names of the markdown files.
    rstLinks : boolean, optional
        Whether to return a list .rst hyperlinks. The default is False.
    preDic : dictionary, optional
        Whether to use a predefined dictionary instead. The default is None.

    Returns
    -------
    ffsDics : dictionary
        A dictionary of two dictionaries with of featured functions as keys and list of
        page titles of the files as values, HyperCells and HyperBloch, respectively.
    """ 
    if preDic:
        pffsDic = preDic
    else: 
        if rstLinks:
            [pffsDic, hyLinks]  = pageffsDict(path, fileNames, rstLinks=rstLinks)
        else:
            pffsDic = pageffsDict(path, fileNames)

    ffspDics = {"HyperCells" : {}, "HyperBloch" : {}}
    for package in ["HyperCells", "HyperBloch"]:
        for key, value in pffsDic[package].items():
            for string in value:
                ffspDics[package].setdefault(string, []).append(key)
        ffspDics[package] = dict(sorted(ffspDics[package].items())) # in alphabetical order
    if rstLinks:
        return [ffspDics, hyLinks]
    else:
        return ffspDics

# ===============================================================================================
# Main functions  :
# ===============================================================================================

def interlinkFile(path, name, ffspDics, filetype=".rst", rstLinks=None):
    """ Create (or overwrite) a file linking featured functions
    to corresponding pages.

    Parameters
    ----------
    path : string
        Absolute path to the markdown interlink file.
    name : string
        Interlink file name.
    ffspDics : dictionary
        Dictionary of two dictionaries with featured functions as keys and
        pages as values, HyperCells and HyperBloch, respectively.
    filetype : string, optional
        File type. The default is .rst.
    rstLinks : array like, optional
        Whether to include a list of .rst hyperlinks in the cerated .rst file. The default is None.
    """ 
    file = open(path + name + filetype, "w")
    file.write(":orphan:\n\n")
    
    if not rstLinks == None:
        for link in rstLinks:
            file.write(f"{link}\n\n")

    colors = {"HyperCells" : "info", "HyperBloch" : "danger"}
    for package, ffspDic in ffspDics.items():
        file.write(f'\n\n.. dropdown:: {package} package:\n   :color: {colors[package]}\n   :icon: package\n\n')
        for k in ffspDic.keys():
            LstToStr = re.sub("'", "", str(ffspDic[k])[1:-1])
            file.write(f"   .. dropdown:: {k}:\n\n      {LstToStr}\n")

# ===============================================================================================