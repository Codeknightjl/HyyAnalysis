import ROOT
ROOT.gInterpreter.ProcessLine(
ROOT.gInterpreter.ProcessLine(
ROOT.gInterpreter.ProcessLine("#include 'TROOT.h'")
ROOT.gInterpreter.ProcessLine("#include 'TSelector.h'")
ROOT.gInterpreter.ProcessLine("#include 'TChain.h'")
ROOT.gInterpreter.ProcessLine("#include 'TFile.h'")
ROOT.gInterpreter.ProcessLine("#include 'TH1.h'")
ROOT.gInterpreter.ProcessLine("#include 'vector'")
class HyyAnalysis(TSelector):
    fChain = TTree('fchain','fchain')
    hist_mYY_bin1 = 0
    hist_mYY_cat_bin1 = 0
    # Declaration of leaf types
    runNumber = 0
    eventNumber = 0
    channelNumber = 0
    mcWeight = 0
    scaleFactor_PILEUP = 0
    scaleFactor_ELE = 0
    scaleFactor_MUON = 0
    scaleFactor_PHOTON = 0
    scaleFactor_TAU = 0
    scaleFactor_BTAG = 0
    scaleFactor_LepTRIGGER = 0
    scaleFactor_PhotonTRIGGER = 0
    scaleFactor_TauTRIGGER = 0
    scaleFactor_DiTauTRIGGER = 0
    trigE = 0
    trigM = 0
    trigP = 0
    trigT = 0
    trigDT = 0
    lep_n = 0
    lep_truthMatched = []
    lep_trigMatched = []
    lep_pt = []
    lep_eta = []
    lep_phi = []
    lep_E = []
    lep_z0 = []
    lep_charge = []
    lep_type = []
    lep_isTightID = []
    lep_ptcone30 = []
    lep_etcone20 = []
    lep_trackd0pvunbiased = []
    lep_tracksigd0pvunbiased = []
    met_et = 0
    met_phi = 0
    jet_n = 0
    jet_pt = []
    jet_eta = []
    jet_phi = []
    jet_E = []
    jet_jvt = []
    jet_trueflav = []
    jet_truthMatched = []
    jet_MV2c10 = []
    photon_n = 0
    photon_truthMatched = []
    photon_trigMatched = []
    photon_pt = []
    photon_eta = []
    photon_phi = []
    photon_E = []
    photon_isTightID = []
    photon_ptcone30 = []
    photon_etcone20 = []
    photon_convType = [] # 0 = unconverted photon, 1 = one track only, with Si hits, 2=one track only, no Si hits (TRT only), 3=two tracks, both with Si hits, 4=two tracks, none with Si hits (TRT only), 5=two tracks, only one with Si hits
    largeRjet_n = 0
    largeRjet_pt = []
    largeRjet_eta = []
    largeRjet_phi = []
    largeRjet_E = []
    largeRjet_m = []
    largeRjet_truthMatched = []
    largeRjet_D2 = []
    largeRjet_tau32 = []
    tau_n = 0
    tau_pt = []
    tau_eta = []
    tau_phi = []
    tau_E = []
    tau_isTightID = []
    tau_truthMatched = []
    tau_trigMatched = []
    tau_nTracks = []
    tau_BDTid = []
    ditau_m = 0
    truth_pt = []
    truth_eta = []
    truth_phi = []
    truth_E = []
    truth_pdgid = []
    lep_pt_syst = []
    met_et_syst = 0
    jet_pt_syst = []
    photon_pt_syst = []
    largeRjet_pt_syst = []
    tau_pt_syst = []

    #List of branches

    fChain.Branch(b_runNumber, 100000, "b_runNumber/F")
    fChain.Branch(b_eventNumber, 100000, "b_eventNumber/F")
    fChain.Branch(b_channelNumber, 100000, "b_channelNumber/F")
    fChain.Branch(b_mcWeight, 100000, "b_mcWeight/F")
    fChain.Branch(b_scaleFactor_PILEUP, 100000, "b_scaleFactor_PILEUP/F")
    fChain.Branch(b_scaleFactor_ELE, 100000, "b_scaleFactor_ELE/F")
    fChain.Branch(b_scaleFactor_MUON, 100000, "b_scaleFactor_MUON/F")
    fChain.Branch(b_scaleFactor_PHOTON, 100000, "b_scaleFactor_PHOTON/F")
    fChain.Branch(b_scaleFactor_TAU, 100000, "b_scaleFactor_TAU/F")
    fChain.Branch(b_scaleFactor_BTAG, 100000, "b_scaleFactor_BTAG/F")
    fChain.Branch(b_scaleFactor_LepTRIGGER, 100000, "b_scaleFactor_LepTRIGGER/F")
    fChain.Branch(b_scaleFactor_PhotonTRIGGER, 100000, "b_scaleFactor_PhotonTRIGGER/F")
    fChain.Branch(b_scaleFactor_TauTRIGGER, 100000, "b_scaleFactor_TauTRIGGER/F")
    fChain.Branch(b_scaleFactor_DiTauTRIGGER, 100000, "b_scaleFactor_DiTauTRIGGER/F")
    fChain.Branch(b_trigE, 100000, "b_trigE/F")
    fChain.Branch(b_trigM, 100000, "b_trigM/F")
    fChain.Branch(b_trigP, 100000, "b_trigP/F")
    fChain.Branch(b_trigT, 100000, "b_trigT/F")
    fChain.Branch(b_trigDT, 100000, "b_trigDT/F")
    fChain.Branch(b_lep_n, 100000, "b_lep_n/F")
    fChain.Branch(b_lep_truthMatched, 100000, "b_lep_truthMatched/F")
    fChain.Branch(b_lep_trigMatched, 100000, "b_lep_trigMatched/F")
    fChain.Branch(b_lep_pt, 100000, "b_lep_pt/F")
    fChain.Branch(b_lep_eta, 100000, "b_lep_eta/F")
    fChain.Branch(b_lep_phi, 100000, "b_lep_phi/F")
    fChain.Branch(b_lep_E, 100000, "b_lep_E/F")
    fChain.Branch(b_lep_z0, 100000, "b_lep_z0/F")
    fChain.Branch(b_lep_charge, 100000, "b_lep_charge/F")
    fChain.Branch(b_lep_type, 100000, "b_lep_type/F")
    fChain.Branch(b_lep_isTightID, 100000, "b_lep_isTightID/F")
    fChain.Branch(b_lep_ptcone30, 100000, "b_lep_ptcone30/F")
    fChain.Branch(b_lep_etcone20, 100000, "b_lep_etcone20/F")
    fChain.Branch(b_lep_trackd0pvunbiased, 100000, "b_lep_trackd0pvunbiased/F")
    fChain.Branch(b_lep_tracksigd0pvunbiased, 100000, "b_lep_tracksigd0pvunbiased/F")
    fChain.Branch(b_met_et, 100000, "b_met_et/F")
    fChain.Branch(b_met_phi, 100000, "b_met_phi/F")
    fChain.Branch(b_jet_n, 100000, "b_jet_n/F")
    fChain.Branch(b_jet_pt, 100000, "b_jet_pt/F")
    fChain.Branch(b_jet_eta, 100000, "b_jet_eta/F")
    fChain.Branch(b_jet_phi, 100000, "b_jet_phi/F")
    fChain.Branch(b_jet_E, 100000, "b_jet_E/F")
    fChain.Branch(b_jet_jvt, 100000, "b_jet_jvt/F")
    fChain.Branch(b_jet_trueflav, 100000, "b_jet_trueflav/F")
    fChain.Branch(b_jet_truthMatched, 100000, "b_jet_truthMatched/F")
    fChain.Branch(b_jet_MV2c10, 100000, "b_jet_MV2c10/F")
    fChain.Branch(b_photon_n, 100000, "b_photon_n/F")
    fChain.Branch(b_photon_truthMatched, 100000, "b_photon_truthMatched/F")
    fChain.Branch(b_photon_trigMatched, 100000, "b_photon_trigMatched/F")
    fChain.Branch(b_photon_pt, 100000, "b_photon_pt/F")
    fChain.Branch(b_photon_eta, 100000, "b_photon_eta/F")
    fChain.Branch(b_photon_phi, 100000, "b_photon_phi/F")
    fChain.Branch(b_photon_E, 100000, "b_photon_E/F")
    fChain.Branch(b_photon_isTightID, 100000, "b_photon_isTightID/F")
    fChain.Branch(b_photon_ptcone30, 100000, "b_photon_ptcone30/F")
    fChain.Branch(b_photon_etcone20, 100000, "b_photon_etcone20/F")
    fChain.Branch(b_photon_convType, 100000, "b_photon_convType/F")
    fChain.Branch(b_largeRjet_n, 100000, "b_largeRjet_n/F")
    fChain.Branch(b_largeRjet_pt, 100000, "b_largeRjet_pt/F")
    fChain.Branch(b_largeRjet_eta, 100000, "b_largeRjet_eta/F")
    fChain.Branch(b_largeRjet_phi, 100000, "b_largeRjet_phi/F")
    fChain.Branch(b_largeRjet_E, 100000, "b_largeRjet_E/F")
    fChain.Branch(b_largeRjet_m, 100000, "b_largeRjet_m/F")
    fChain.Branch(b_largeRjet_truthMatched, 100000, "b_largeRjet_truthMatched/F")
    fChain.Branch(b_largeRjet_D2, 100000, "b_largeRjet_D2/F")
    fChain.Branch(b_largeRjet_tau32, 100000, "b_largeRjet_tau32/F")
    fChain.Branch(b_tau_n, 100000, "b_tau_n/F")
    fChain.Branch(b_tau_pt, 100000, "b_tau_pt/F")
    fChain.Branch(b_tau_eta, 100000, "b_tau_eta/F")
    fChain.Branch(b_tau_phi, 100000, "b_tau_phi/F")
    fChain.Branch(b_tau_E, 100000, "b_tau_E/F")
    fChain.Branch(b_tau_isTightID, 100000, "b_tau_isTightID/F")
    fChain.Branch(b_tau_truthMatched, 100000, "b_tau_truthMatched/F")
    fChain.Branch(b_tau_trigMatched, 100000, "b_tau_trigMatched/F")
    fChain.Branch(b_tau_nTracks, 100000, "b_tau_nTracks/F")
    fChain.Branch(b_tau_BDTid, 100000, "b_tau_BDTid/F")
    fChain.Branch(b_ditau_m, 100000, "b_ditau_m/F")
    fChain.Branch(b_truth_pt, 100000, "b_truth_pt/F")
    fChain.Branch(b_truth_eta, 100000, "b_truth_eta/F")
    fChain.Branch(b_truth_phi, 100000, "b_truth_phi/F")
    fChain.Branch(b_truth_E, 100000, "b_truth_E/F")
    fChain.Branch(b_truth_pdgid, 100000, "b_truth_pdgid/F")
    fChain.Branch(b_lep_pt_syst, 100000, "b_lep_pt_syst/F")
    fChain.Branch(b_met_et_syst, 100000, "b_met_et_syst/F")
    fChain.Branch(b_jet_pt_syst, 100000, "b_jet_pt_syst/F")
    fChain.Branch(b_photon_pt_syst, 100000, "b_photon_pt_syst/F")
    fChain.Branch(b_largeRjet_pt_syst, 100000, "b_largeRjet_pt_syst/F")
    fChain.Branch(b_tau_pt_syst, 100000, "b_tau_pt_syst/F")

    def version(self):
        return 2
    def Begin(self, tree):
    def SlaveBegin(self, tree):
    def Init(self, tree):
    def Notify(self):
    def Process(self,entry):
    def GetEntry(self,entry,getall=0):
        if fChain == True:
            return fChain.GetTree().GetEntry(entry,getall)
        else:
            return 0
    def SetOption(self, option):
        fOption = option
    def SetObject(self,obj):
        fObject = obj
    def SetInputList(self,input):
        fInput = input
    def FillHistogramsGlobal(self, m, w, s):

    #Get Output List to save our histograms in the output file
    def GetOutputLisr(self):
        return fOutput
    def define_histograms(self):
        return
    def FillOutputList(self):
        return
    def WriteHistograms(self):
        return
    def SlaveTerminate(self):
        return
    def Terminate(self):
        return

    nEvents = 0
    nEvent = 0
    nEvent2 = 0
    nEvent3 = 0
    nEvent4 = 0
    nEvent5 = 0
    nEvent6 = 0

    ClassDef(HyyAnalysis,0)
    tree = TTree('tree','tree')
def Init(tree):
    lep_truthMatched = 0
    lep_trigMatched = 0
    lep_pt = 0
    lep_eta = 0
    lep_phi = 0
    lep_E = 0
    lep_z0 = 0
    lep_charge = 0
    lep_type = 0
    lep_isTightID = 0
    lep_ptcone30 = 0
    lep_etcone20 = 0
    lep_trackd0pvunbiased = 0
    lep_tracksigd0pvunbiased = 0
    jet_pt = 0
    jet_eta = 0
    jet_phi = 0
    jet_E = 0
    jet_jvt = 0
    jet_trueflav = 0
    jet_truthMatched = 0
    jet_MV2c10 = 0
    photon_truthMatched = 0
    photon_trigMatched = 0
    photon_pt = 0
    photon_eta = 0
    photon_phi = 0
    photon_E = 0
    photon_isTightID = 0
    photon_ptcone30 = 0
    photon_etcone20 = 0
    photon_convType = 0
    largeRjet_pt = 0
    largeRjet_eta = 0
    largeRjet_phi = 0
    largeRjet_E = 0
    largeRjet_m = 0
    largeRjet_truthMatched = 0
    largeRjet_D2 = 0
    largeRjet_tau32 = 0
    tau_pt = 0
    tau_eta = 0
    tau_phi = 0
    tau_E = 0
    tau_isTightID = 0
    tau_truthMatched = 0
    tau_trigMatched = 0
    tau_nTracks = 0
    tau_BDTid = 0
    truth_pt = 0
    truth_eta = 0
    truth_phi = 0
    truth_E = 0
    truth_pdgid = 0
    lep_pt_syst = 0
    jet_pt_syst = 0
    photon_pt_syst = 0
    largeRjet_pt_syst = 0
    tau_pt_syst = 0

    #Set branch addresses and branch pointers
    if not tree:
        return
    fChain = tree
    fChain.SetMakeClass(1)

    fChain.SetBranchAddress("runNumber", id(runNumber), id(b_runNumber))
    fChain.SetBranchAddress("eventNumber", id(eventNumber), id(b_eventNumber))
    fChain.SetBranchAddress("channelNumber", id(channelNumber), id(b_channelNumber))
    fChain.SetBranchAddress("mcWeight", id(mcWeight), id(b_mcWeight))
    fChain.SetBranchAddress("scaleFactor_PILEUP", id(scaleFactor_PILEUP), id(b_scaleFactor_PILEUP))
    fChain.SetBranchAddress("scaleFactor_ELE", id(scaleFactor_ELE), id(b_scaleFactor_ELE))
    fChain.SetBranchAddress("scaleFactor_MUON", id(scaleFactor_MUON), id(b_scaleFactor_MUON))
    fChain.SetBranchAddress("scaleFactor_PHOTON", id(scaleFactor_PHOTON), id(b_scaleFactor_PHOTON))
    fChain.SetBranchAddress("scaleFactor_TAU", id(scaleFactor_TAU), id(b_scaleFactor_TAU))
    fChain.SetBranchAddress("scaleFactor_BTAG", id(scaleFactor_BTAG), id(b_scaleFactor_BTAG))
    fChain.SetBranchAddress("scaleFactor_LepTRIGGER", id(scaleFactor_LepTRIGGER), id(b_scaleFactor_LepTRIGGER))
    fChain.SetBranchAddress("scaleFactor_PhotonTRIGGER", id(scaleFactor_PhotonTRIGGER), id(b_scaleFactor_PhotonTRIGGER))
    fChain.SetBranchAddress("trigE", id(trigE), id(b_trigE))
    fChain.SetBranchAddress("trigM", id(trigM), id(b_trigM))
    fChain.SetBranchAddress("trigP", id(trigP), id(b_trigP))
    fChain.SetBranchAddress("lep_n", id(lep_n), id(b_lep_n))
    fChain.SetBranchAddress("lep_truthMatched", id(lep_truthMatched), id(b_lep_truthMatched))
    fChain.SetBranchAddress("lep_trigMatched", id(lep_trigMatched), id(b_lep_trigMatched))
    fChain.SetBranchAddress("lep_pt", id(lep_pt), id(b_lep_pt))
    fChain.SetBranchAddress("lep_eta", id(lep_eta), id(b_lep_eta))
    fChain.SetBranchAddress("lep_phi", id(lep_phi), id(b_lep_phi))
    fChain.SetBranchAddress("lep_E", id(lep_E), id(b_lep_E))
    fChain.SetBranchAddress("lep_z0", id(lep_z0), id(b_lep_z0))
    fChain.SetBranchAddress("lep_charge", id(lep_charge), id(b_lep_charge))
    fChain.SetBranchAddress("lep_type", id(lep_type), id(b_lep_type))
    fChain.SetBranchAddress("lep_isTightID", id(lep_isTightID), id(b_lep_isTightID))
    fChain.SetBranchAddress("lep_ptcone30", id(lep_ptcone30), id(b_lep_ptcone30))
    fChain.SetBranchAddress("lep_etcone20", id(lep_etcone20), id(b_lep_etcone20))
    fChain.SetBranchAddress("lep_trackd0pvunbiased", id(lep_trackd0pvunbiased), id(b_lep_trackd0pvunbiased))
    fChain.SetBranchAddress("lep_tracksigd0pvunbiased", id(lep_tracksigd0pvunbiased), id(b_lep_tracksigd0pvunbiased))
    fChain.SetBranchAddress("met_et", id(met_et), id(b_met_et))
    fChain.SetBranchAddress("met_phi", id(met_phi), id(b_met_phi))
    fChain.SetBranchAddress("jet_n", id(jet_n), id(b_jet_n))
    fChain.SetBranchAddress("jet_pt", id(jet_pt), id(b_jet_pt))
    fChain.SetBranchAddress("jet_eta", id(jet_eta), id(b_jet_eta))
    fChain.SetBranchAddress("jet_phi", id(jet_phi), id(b_jet_phi))
    fChain.SetBranchAddress("jet_E", id(jet_E), id(b_jet_E))
    fChain.SetBranchAddress("jet_jvt", id(jet_jvt), id(b_jet_jvt))
    fChain.SetBranchAddress("jet_trueflav", id(jet_trueflav), id(b_jet_trueflav))
    fChain.SetBranchAddress("jet_truthMatched", id(jet_truthMatched), id(b_jet_truthMatched))
    fChain.SetBranchAddress("jet_MV2c10", id(jet_MV2c10), id(b_jet_MV2c10))
    fChain.SetBranchAddress("photon_n", id(photon_n), id(b_photon_n))
    fChain.SetBranchAddress("photon_truthMatched", id(photon_truthMatched), id(b_photon_truthMatched))
    fChain.SetBranchAddress("photon_trigMatched", id(photon_trigMatched), id(b_photon_trigMatched))
    fChain.SetBranchAddress("photon_pt", id(photon_pt), id(b_photon_pt))
    fChain.SetBranchAddress("photon_eta", id(photon_eta), id(b_photon_eta))
    fChain.SetBranchAddress("photon_phi", id(photon_phi), id(b_photon_phi))
    fChain.SetBranchAddress("photon_E", id(photon_E), id(b_photon_E))
    fChain.SetBranchAddress("photon_isTightID", id(photon_isTightID), id(b_photon_isTightID))
    fChain.SetBranchAddress("photon_ptcone30", id(photon_ptcone30), id(b_photon_ptcone30))
    fChain.SetBranchAddress("photon_etcone20", id(photon_etcone20), id(b_photon_etcone20))
    fChain.SetBranchAddress("photon_convType", id(photon_convType), id(b_photon_convType))
    fChain.SetBranchAddress("lep_pt_syst", id(lep_pt_syst), id(b_lep_pt_syst))
    fChain.SetBranchAddress("met_et_syst", id(met_et_syst), id(b_met_et_syst))
    fChain.SetBranchAddress("jet_pt_syst", id(jet_pt_syst), id(b_jet_pt_syst))
    fChain.SetBranchAddress("photon_pt_syst", id(photon_pt_syst), id(b_photon_pt_syst))
    fChain.SetBranchAddress("largeRjet_pt_syst", id(largeRjet_pt_syst), id(b_largeRjet_pt_syst))
    fChain.SetBranchAddress("tau_pt_syst", id(tau_pt_syst), id(b_tau_pt_syst))


def Notify():

# The Notify() function is called when a new file is opened. This
# can be either for a new TTree in a TChain or when when a new TTree
# is started when using PROOF. It is normally not necessary to make changes
# to the generated code, but the routine can be extended by the
# user if needed. The return value is currently not used.

  return kTRUE

