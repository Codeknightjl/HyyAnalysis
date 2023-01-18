# PyROOT Framework for ATLAS Open Data Analysis of Higgs to Two Photons Decay Channel

### Introduction
This framework analyzes the decay channel of a Higgs boson into two photons from the 13 TeV ATLAS Open Data. It uses the Python interfaced for ROOT known as [PyROOT]([url](https://root.cern/manual/python/)). This Python rendering is modified from the [C++ framework]([url](https://github.com/atlas-outreach-data-tools/atlas-outreach-cpp-framework-13tev)) released in the [13 TeV ATLAS Open Data documentation]([url](http://opendata.atlas.cern/release/2020/documentation/index.html)). It emulates the procedures used in actual High Energy Physics research.

### Analysis
This decay mode provides a clear signature of two isolated and energetic photons. The signal manifests itself as a narrow peak in the diphoton invariant mass spectrum on top of a smoothly falling background from QCD production of two photons. More information can be found in the official documentation. (see reference)

The procedures for the analysis:
 - Apply the standard object-selection criteria and an event-selection criteria to identify the photons.
 - Compare data and Monte-Carlo prediction for the distribution of the diphoton invariant mass spectrum.
 - Find an excess of events (a bump) in the histogram of event distribution.
 - The location of the excess of events gives the mass of the Higgs Boson.
 
### Reference
 
PyROOT Documentation: https://root.cern/manual/python/    
H->yy decay channel analysis description: http://opendata.atlas.cern/release/2020/documentation/physics/YY.html       
H->yy analysis framework in C++: http://opendata.atlas.cern/release/2020/documentation/physics/YY.html
