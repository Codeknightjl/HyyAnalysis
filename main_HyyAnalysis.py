import ROOT
ROOT.gInterpreter.ProcessLine('#include TROOT.h')
ROOT.gInterpreter.ProcessLine('#include TChain.h')
ROOT.gInterpreter.ProcessLine('#include TFile.h')
ROOT.gInterpreter.ProcessLine('#include TProof.h')
def main_HyyAnalysis(proof = 0, option = 0):
    path = ROOT.TString("")
    if proof == 1:
        ROOT.TProof.Open()
    if option == 1 or option == 0:
        chain_data = ROOT.TChain("mini")
        chain_data.AddFile(path + "Data/data_A.GamGam.root")
        chain_data.AddFile(path + "Data/data_B.GamGam.root")
        chain_data.AddFile(path + "Data/data_C.GamGam.root")
        chain_data.AddFile(path + "Data/data_D.GamGam.root")
        if proof == 1:
            chain_data.SetProof()
        chain_data.Process("HyyAnalysis.C+", "data")
    if option == 0 or option == 2:
        chain_ggH125 = ROOT.TChain("mini")
        chain_ggH125.AddFile(path + "MC/mc_343981.ggH125_gamgam.GamGam.root")
        if  proof == 1:
            chain_ggH125.SetProof()
        chain_ggH125.Process("HyyAnalysis.C+","ggH125_gamgam")
        #VBF Higgs Production
        chain_VBFH125 = ROOT.TChain("mini")
        chain_VBFH125.AddFile(path + "MC/mc_345041.VBFH125_gamgam.GamGam.root");
        if proof == 1:
            chain_VBFH125.SetProof()
        chain_VBFH125.Process("HyyAnalysis.C+", "VBFH125_gamgam")
        #WH production
        chain_WH125 = ROOT.TChain("mini")
        chain_WH125.AddFile(path + "MC/mc_345318.WpH125J_Wincl_gamgam.GamGam.root")
        if proof == 1:
            chain_WH125.SetProof()
        chain_WH125.Process("HyyAnalysis.C+", "WH125_gamgam")
        #ZH production
        chain_ZH125 = ROOT.TChain("mini")
        chain_ZH125.AddFile(path + "MC/mc_345319.ZH125J_Zincl_gamgam.GamGam.root");
        if proof == 1:
            chain_ZH125.SetProof()
        chain_ZH125.Process("HyyAnalysis.C+", "ZH125_gamgam")
        #ttH production
        chain_ttH125 = ROOT.TChain("mini")
        chain_ttH125.AddFile(path + "MC/mc_341081.ttH125_gamgam.GamGam.root");
        if proof == 1:
            chain_ttH125.SetProof()
        chain_ttH125.Process("HyyAnalysis.C+", "ttH125_gamgam")
