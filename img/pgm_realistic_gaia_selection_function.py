"""
Realistic Gaia selection function as probabilistic graphical model.

Anthony Brown Feb 2020
"""

from matplotlib import rc
import matplotlib.pyplot as plt
rc("font", family="serif", size=13)
rc("text", usetex=False)

import daft

pgm = daft.PGM([12.75,7.5], origin=[-1, 2], node_unit=1.5, grid_unit=2.5)

pgm.add_node(daft.Node("Gsource", "$G_\mathrm{source}$", 0, 8, aspect=1.2))
pgm.add_node(daft.Node("detection", "detection and\nreal/spurious\ndiscrimination", 4, 7, aspect=3.8))
pgm.add_node(daft.Node("Gvpu", "$G_\mathrm{VPU}$", 2.5, 8))
pgm.add_node(daft.Node("confirmation", "confirmation", 4, 6, aspect=2.25))
pgm.add_node(daft.Node("afxpobs", "AF/XP\nobservations", 4, 5, aspect=2.5))
pgm.add_node(daft.Node("rvsobs", "RVS \nobservations", 4, 4, aspect=2.5))
pgm.add_node(daft.Node("GRVSsource", "$G_\mathrm{RVS,source}$", 0, 4, aspect=1.75))
pgm.add_node(daft.Node("bpminrp", "$(G_\mathrm{BP}-G_\mathrm{RP})_\mathrm{source}$", 0, 3, aspect=2.75))
pgm.add_node(daft.Node("GRVSvpu", "$G_\mathrm{RVS,VPU}$", 2.5, 4, aspect=1.5))
pgm.add_node(daft.Node("sp", "Tel. Packets\non ground", 6.5, 4.5, aspect=2.5))
pgm.add_node(daft.Node("realspurious", "Real/spurious\nclassification", 6.5, 5.5, aspect=2.8,
    plot_params={"ec":plt.cm.tab10.colors[1], "lw":2}))
pgm.add_node(daft.Node("match", "Observation to\nsource matching", 6.5, 6.5, aspect=3.00,
    plot_params={"ec":plt.cm.tab10.colors[1], "lw":2}))
pgm.add_node(daft.Node("sourcelist", "Source\nlist", 6.5, 7.5, aspect=1.5, plot_params={"ec":plt.cm.tab10.colors[1],
    "lw":2}))
pgm.add_node(daft.Node("pipeline", "Processing\npipeline\nfilters", 8.5, 7.5, aspect=3.25,
    plot_params={"ec":plt.cm.tab10.colors[1], "lw":2}))
pgm.add_node(daft.Node("validation", "Data\nquality\nfilters", 8.5, 6.5, aspect=2.5,
    plot_params={"ec":plt.cm.tab10.colors[1], "lw":2}))
pgm.add_node(daft.Node("catalogue", "Gaia\ncatalogue", 8.5, 5.5, aspect=2.0, plot_params={"ec":plt.cm.tab10.colors[1],
    "lw":2}))
pgm.add_node(daft.Node("sourceAPs", "Source\nastrophysical\nparameters", 10.5, 7.0, aspect=3.0,
    plot_params={"ec":plt.cm.tab10.colors[1], "lw":2}))

pgm.add_node(daft.Node("scanlaw", "Actual\nscan law", 5, 9, fixed=True))
pgm.add_node(daft.Node("events", "S/C+Payload\noutages", 4, 9, fixed=True))
pgm.add_node(daft.Node("fovhist", "FoV\nhistory", 4.5, 8, fixed=True, offset=(0,-40)))
pgm.add_node(daft.Node("Gvpulim", "$G_\mathrm{VPU,lim}$", 1, 7, fixed=True, offset=(0,6)))
pgm.add_node(daft.Node("resource", "VPU resource\nmanagement", 1, 6, fixed=True, offset=(-12,6)))
pgm.add_node(daft.Node("fpamotion", "Focal plane\nmotion", 1, 5, fixed=True, offset=(0,6)))
pgm.add_node(daft.Node("Gvpurvslim", "Variable\n$G_\mathrm{RVS,VPU,lim}$", 4, 3, fixed=True, offset=(0,-36)))
pgm.add_node(daft.Node("telemetry", "Ground station time +\nOn-board storage\nlimitations,\nTelemetry losses", 6.5, 3,
    fixed=True, offset=(0,-66)))
pgm.add_node(daft.Node("sigmaG", "$\sigma_{G_\mathrm{VPU}}$", 1.5, 8.5, fixed=True, aspect=1, offset=(0,6)))
pgm.add_node(daft.Node("sigmaGRVS", "$\sigma_{G_\mathrm{RVS,VPU}}$", 2.5, 3.0, fixed=True, aspect=1, offset=(0,-36)))

pgm.add_edge("Gsource", "Gvpu")
pgm.add_edge("Gsource", "GRVSsource")
pgm.add_edge("fovhist", "Gvpu")
pgm.add_edge("Gvpu", "detection")
pgm.add_edge("Gvpulim", "detection")
pgm.add_edge("events", "fovhist")
pgm.add_edge("scanlaw", "fovhist")
pgm.add_edge("detection", "confirmation")
pgm.add_edge("confirmation", "afxpobs")
pgm.add_edge("afxpobs", "rvsobs")
pgm.add_edge("resource", "afxpobs")
pgm.add_edge("resource", "rvsobs")
pgm.add_edge("resource", "detection")
pgm.add_edge("fpamotion", "afxpobs")
pgm.add_edge("fpamotion", "rvsobs")
pgm.add_edge("GRVSsource", "GRVSvpu")
pgm.add_edge("bpminrp", "GRVSsource")
pgm.add_edge("Gvpu", "GRVSvpu")
pgm.add_edge("GRVSvpu", "rvsobs")
pgm.add_edge("Gvpurvslim", "rvsobs")
pgm.add_edge("afxpobs", "sp")
pgm.add_edge("rvsobs", "sp")
pgm.add_edge("telemetry", "sp")
pgm.add_edge("sp", "realspurious")
pgm.add_edge("realspurious", "match")
pgm.add_edge("match", "sourcelist")
pgm.add_edge("sourcelist", "pipeline")
pgm.add_edge("pipeline", "validation")
pgm.add_edge("validation", "catalogue")
pgm.add_edge("sourceAPs", "pipeline")
pgm.add_edge("sourceAPs", "validation")
pgm.add_edge("sigmaG", "Gvpu")
pgm.add_edge("sigmaGRVS", "GRVSvpu")

pgm.add_plate([5.5, 5.0, 6.0, 3], label="On-ground\nprocessing\nstrongly\nsimplified", position="bottom right", shift=0, fontsize=10)

pgm.render()
pgm.figure.savefig("pgm_realistic_gsf.pdf")
pgm.figure.savefig("pgm_realistic_gsf.png", dpi=150)
