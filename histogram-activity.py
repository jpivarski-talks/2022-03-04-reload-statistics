# git clone https://github.com/boostorg/histogram.git
# git clone https://github.com/cbourjau/pyhistogram.git
# git clone https://github.com/CoffeaTeam/coffea.git
# git clone https://github.com/histogrammar/histogrammar-python.git
# git clone https://github.com/ibab/matplotlib-hep.git
# git clone https://github.com/janpipek/physt.git
# git clone https://github.com/JelleAalbers/multihist.git
# git clone https://github.com/jpivarski/plothon.git
# git clone https://github.com/jpivarski/svgfig.git
# git clone https://github.com/ndevenish/simplehistogram.git
# git clone https://github.com/root-project/root.git
# git clone https://github.com/rootpy/rootpy.git
# git clone https://github.com/scikit-hep/boost-histogram.git
# git clone https://github.com/scikit-hep/histbook.git
# git clone https://github.com/scikit-hep/hist.git
# git clone https://github.com/scikit-hep/mplhep.git
# git clone https://gitlab.com/ckhurewa/qhist.git
# git clone https://gitlab.com/hepcedar/yoda.git

import csv

import git

restrictions = {
    "root": [
        "TH1",
        "TH1C",
        "TH1D",
        "TH1F",
        "TH1I",
        "TH1K",
        "TH1S",
        "TProfile",
        "TH2",
        "TH2C",
        "TH2D",
        "TH2F",
        "TH2I",
        "TH2S",
        "TProfile2D",
        "TH2Poly",
        "TProfile2Poly",
        "TH3",
        "TH3C",
        "TH3D",
        "TH3F",
        "TH3I",
        "TH3S",
        "TProfile3D",
        "TGLTH3Composition",
        "THn",
        "THnBase",
        "THnSparse",
        "THnSparse_Internal",
        "THnChain",
        "TEfficiency",
        "THStack",
        "TKDE",
        "TUnfold",
        "TUnfoldSys",
        "TUnfoldDensity",
        "TSVDUnfold",
        "TConfidenceLevel",
        "TAxis",
        "TAxisModLab",
        "TVirtualHistPainter",
        "THistPainter",
        "THistRange",
        "Haxis",
        "RAxis",
        "RAxisConfig",
        "RHist",
        "RHistBinIter",
        "RHistBufferedFill",
        "RHistConcurrentFill",
        "RHistData",
        "RHistImpl",
        "RHistUtils",
        "RHistView",
        "RHistDraw7Provider",
        "RHistBinIter",
    ],
    "coffea": [
        "hist",
    ],
    "rootpy": [
        "hist.py",
        "views.py",
        "root2matplotlib.py",
    ],
}

with open("histogram-activity.csv", "w") as output:
    writer = csv.writer(output)
    writer.writerow([
        "package",
        "date",
        "author",
        "file",
        "insertions",
        "deletions",
    ])

    for package in [
        "simplehistogram",
        "plothon",
        "matplotlib-hep",
        "pyhistogram",
        "multihist",
        "svgfig",
        "histbook",
        "qhist",
        "boost-histogram",
        "hist",
        "histogram",
        "yoda",
        "mplhep",
        "rootpy",
        "physt",
        "coffea",
        "histogrammar-python",
        "root",
    ]:
        repo = git.Repo(package)
        restriction = restrictions.get(package, None)
        for commit in repo.iter_commits():
            date = commit.committed_date
            author = commit.author.email
            for file, stats in commit.stats.files.items():
                if restriction is None or any(x in file for x in restriction):
                    insertions = stats["insertions"]
                    deletions = stats["deletions"]
                    writer.writerow([
                        package,
                        date,
                        author,
                        file,
                        insertions,
                        deletions,
                    ])
