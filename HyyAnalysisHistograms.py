import ROOT
ROOT.gInterpreter.ProcessLine('#include TROOT.h')
ROOT.gInterpreter.ProcessLine('#include TH1.h')
ROOT.gInterpreter.ProcessLine('#include TH2.h')
ROOT.gInterpreter.ProcessLine('#include TH3.h')
ROOT.gInterpreter.ProcessLine('#include <iostream>')
def define_histograms(self):
    hist_mYY_bin1 = ROOT.TH1F("hist_mYY_bin1", "Diphoton invariant mass; m_{#gamma#gamma} [GeV];Events / bin", 30, 105, 160.)
    hist_mYY_cat_bin1 = ROOT.TH1F("hist_mYY_cat_bin1", "Diphoton invariant mass unconv. central; m_{#gamma#gamma} [GeV];Events / bin", 30, 105,
         160.)
def FillOutputList(self):
    GetOutputList().Add(hist_mYY_bin1)
    GetOutputList().Add(hist_mYY_cat_bin1)
def WriteHistograms(self):
    hist_mYY_bin1.Write()
    hist_mYY_cat_bin1.Write()
def FillHistogramsGlobal(self,m,w,s):
    if s.Contains("hist_mYY_bin1"):
        hist_mYY_bin1->Fill(m, w)
    if s.Contains("hist_mYY_cat_bin1"):
        hist_mYY_cat_bin1->Fill(m, w)
HyyAnalysis.define_histograms = define_histograms
HyyAnalysis.FillOutputList = FillOutputList
HyyAnalysis.WriteHistograms = WriteHistograms
HyyAnalysis.FillHistogramsGlobal = FillHistogramsGlobal

