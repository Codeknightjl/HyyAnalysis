import ROOT
ROOT.gInterpreter.ProcessLine("#define HyyAnalysis_cxx")

ROOT.gInterpreter.ProcessLine("#include 'HyyAnalysis.h'")
ROOT.gInterpreter.ProcessLine("#include 'HyyAnalysisHistograms.h'")
ROOT.gInterpreter.ProcessLine("#include <iostream>")
ROOT.gInterpreter.ProcessLine("#include <cstring>")
ROOT.gInterpreter.ProcessLine("#include <string>")

ROOT.gInterpreter.ProcessLine("#include <TH1.h>")
ROOT.gInterpreter.ProcessLine("#include <TH2.h>")
ROOT.gInterpreter.ProcessLine("#include <TStyle.h>")
ROOT.gInterpreter.ProcessLine("#include <TMath.h>")
ROOT.gInterpreter.ProcessLine("#include <TLorentzVector.h>")
ROOT.gInterpreter.ProcessLine("#include <TLorentzVector.h>")

name = ""

def Begin(self):
    nEvents = 0
    nEvent = 0
    nEvent2 = 0
    nEvent3 = 0
    nEvent4 = 0
    nEvent5 = 0

def SlaveBegin(self):
    option = GetOption()
    print("Starting analysis with process option: %s \n", option.Data())
    name = option
    define_histograms()
    FillOutputList()

def Process(self, entry):
    fChain.GetTree().GetEntry(entry)
    nEvent +=1
    nEvents += 1
    if nEvents % 50000 == 0:
        print("Analysed a total of: " + nEvents + " events out of " + fChain.GetTree().GetEntries() + " in this sample\n")
    if fChain.GetTree().GetEntries > 0:
        # ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** //
        # Begin analysis selection, largely based on: ATLAS Collaboration, PRD 98(2018) 052005
        # ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** //

        # Scale factors
        scaleFactor = scaleFactor_PHOTON * scaleFactor_PhotonTRIGGER * scaleFactor_PILEUP

        # MC weight Float_t
        m_mcWeight = mcWeight

        #Total weight
        weight = scaleFactor * m_mcWeight

        # Make difference between data and MC
        option = Getoption()
        if option.Contains("data")):
            weight = 1

        #Preselection cut for photon trigger
        if trigP:
            nEvent2 += 1 #counter
            #Preselection of good photons
            goodphoton_index = []
            goodphoton_n = 0
            photon_index = 0

            for i in range(0,photon_n):
                #photons are tight
                if photon_is_TightID.at(i):
                    if photon_pt.at(i) > 25000 and TMath.Abs(photon_eta.at(i)) < 2.37 and TMaths.Abs(photon_eta.at(i) < 1.37) or TMath.Abs()(photon_eta.at9i) > 1.52:
                        goodphoton_n = goodphoton_n + 1
                        goodphoton_index[photon_index] = i
                        photon_index += 1

            #Exactly two photons
        if goodphoton_n == 2:
            nEvent3 += 1 #counter
            goodphoton1_index = goodphoton_index[0]
            goodphoton2_index = goodphoton_index[1]

            #isolated photons
            if ((photon_ptcone30.at(goodphoton1_index) / photon_pt.at(goodphoton1_index)) < 0.065) and ((photon_etcone20.at(goodphoton1_index) / photon_pt.at(goodphoton1_index)) < 0.065 )):
                if (((photon_ptcone30.at(goodphoton2_index) / photon_pt.at(goodphoton2_index)) < 0.065) and ( (photon_etcone20.at(goodphoton2_index) / photon_pt.at(goodphoton2_index)) < 0.065 )):
                    nEvent4 += 1 #counter

                    #create 2 vectors
                    Photon_1 = TLorentzVector()
                    Photon_2 = TLorentzVector()

                    Photon_1.SetPtEtaPhiE(photon_pt.at(goodphoton1_index), photon_eta.at(goodphoton1_index), photon_phi.at(goodphoton1_index), photon_E.at(goodphoton1_index))
                    Photon_2.SetPtEtaPhiE(photon_pt.at(goodphoton2_index), photon_eta.at(goodphoton2_index), photon_phi.at(goodphoton2_index), photon_E.at(goodphoton2_index))

                    #calculate dPhi(photon - photon)
                    dPhi_yy = TMath.Abs(photon_phi.at(goodphoton1_index) - photon_phi.at(goodphoton2_index))
                    if dPhi_yy >= TMath.Pi():
                        dPhi_yy = 2 * TMath.Pi() - dPhi_yy

                    #diphoton mass
                    m_yy = sqrt(2 * Photon_1.Pt() / 1000 * Photon_2.Pt() / 1000 * (cosh(Photon_1.Eta() - Photon_2.Eta()) - cos(dPhi_yy)));
                    # kinematics
                    Photon_1_kin = Photon_1.Pt() / 1000 / m_yy
                    Photon_2_kin = Photon_2.Pt() / 1000 / m_yy

                    #kinematical selection
                    if Photon_1_kin > 0.35 and Photon_2_kin > 0.25:
                        nEvent5 += 1 #counter

                        #mass-window cut
                        if m_yy > 105 and m_yy < 160:
                            FillHistogramsGlobal(m_yy, weight, "hist_mYY_bin1") #30 bins
                            nEvent6 += 1 #counter

                            #uncovered central category
                            if TMath.Abs(photon_eta.at(goodphoton1_index) < 0.75 and TMath.Abs(photon_eta.at(goodphoton2_index)) < 0.75 and photon_convType.at(goodphoton1_index)==0 and photon_convType.at(goodphoton2_index)==0:
                                FillHistogramsglobal(m_yy,weight,"hist_mYY_cat_bin1") #30 bins

    return kTRUE

def SlaveTerminate(self):
    return

def Terminate(self):
    #Print counters (in case of local, not PROOF)

    #Save output
    filename_option = GetOption()
    print("Writing with name option: " + filename_option.Data() + "\n")
    output_name = "Output_HyyAnalysis/" + filename_option + ".root"
    filename = output_name
    physicsoutput(filename,"recreate")
    WriteHistograms()
    physicsoutput.Close()
