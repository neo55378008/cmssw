############################################################
# define basic process
############################################################

import FWCore.ParameterSet.Config as cms
import os
import sys
process = cms.Process("L1TrackNtuple")

name = 'SingleMuon_noPU_'
layers = str(sys.argv[2])
#if layers == 'L1L2': sys.exit(0) 
name += layers + '_'
#if not arg: name+='Seed.root'
name += 'Seed.root'
print name
 

############################################################
# import standard configurations
############################################################

process.load('Configuration.StandardSequences.Services_cff')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('Configuration.Geometry.GeometryExtended2023TTIReco_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_PostLS1_cff')
process.load('Configuration.StandardSequences.L1TrackTrigger_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
process.load('Geometry.TrackerGeometryBuilder.StackedTrackerGeometry_cfi')

from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'PH2_1K_FB_V3::All', '')


############################################################
# input and output
############################################################

process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(-1))
#Source_Files = cms.untracked.vstring( TheInputFile
Source_Files = cms.untracked.vstring(
    ## single muons PU=0
    '/store/group/comm_trigger/L1TrackTrigger/620_SLHC10/Extended2023TTI/Muons/NoPU/SingleMuon_DIGI_1.root',
    #'/store/group/comm_trigger/L1TrackTrigger/620_SLHC10/Extended2023TTI/Muons/NoPU/SingleMuon_DIGI_2.root',
    #'/store/group/comm_trigger/L1TrackTrigger/620_SLHC10/Extended2023TTI/Muons/NoPU/SingleMuon_DIGI_3.root',
    #'/store/group/comm_trigger/L1TrackTrigger/620_SLHC10/Extended2023TTI/Muons/NoPU/SingleMuon_DIGI_4.root',
    #'/store/group/comm_trigger/L1TrackTrigger/620_SLHC10/Extended2023TTI/Muons/NoPU/SingleMuon_DIGI_5.root',
    #'/store/group/comm_trigger/L1TrackTrigger/620_SLHC10/Extended2023TTI/Muons/NoPU/SingleMuon_DIGI_6.root',
    #'/store/group/comm_trigger/L1TrackTrigger/620_SLHC10/Extended2023TTI/Muons/NoPU/SingleMuon_DIGI_7.root',
    #'/store/group/comm_trigger/L1TrackTrigger/620_SLHC10/Extended2023TTI/Muons/NoPU/SingleMuon_DIGI_8.root',
    #'/store/group/comm_trigger/L1TrackTrigger/620_SLHC10/Extended2023TTI/Muons/NoPU/SingleMuon_DIGI_9.root',
    #'/store/group/comm_trigger/L1TrackTrigger/620_SLHC10/Extended2023TTI/Muons/NoPU/SingleMuon_DIGI_10.root',
    ## single muons PU=140
    #'/store/mc/TTI2023Upg14D/SingleMuMinusFlatPt0p2To150/GEN-SIM-DIGI-RAW/PU140bx25_PH2_1K_FB_V3-v2/00000/0097A61E-04E7-E311-824C-003048678F9C.root',
    ## single electrons PU=0
    #'/store/group/comm_trigger/L1TrackTrigger/620_SLHC10/Extended2023TTI/Electrons/NoPU/SingleElectron_DIGI_1.root',
    #'/store/group/comm_trigger/L1TrackTrigger/620_SLHC10/Extended2023TTI/Electrons/NoPU/SingleElectron_DIGI_2.root',
    #'/store/group/comm_trigger/L1TrackTrigger/620_SLHC10/Extended2023TTI/Electrons/NoPU/SingleElectron_DIGI_3.root',
    #'/store/group/comm_trigger/L1TrackTrigger/620_SLHC10/Extended2023TTI/Electrons/NoPU/SingleElectron_DIGI_4.root',
    #'/store/group/comm_trigger/L1TrackTrigger/620_SLHC10/Extended2023TTI/Electrons/NoPU/SingleElectron_DIGI_5.root',
    #'/store/group/comm_trigger/L1TrackTrigger/620_SLHC10/Extended2023TTI/Electrons/NoPU/SingleElectron_DIGI_6.root',
    #'/store/group/comm_trigger/L1TrackTrigger/620_SLHC10/Extended2023TTI/Electrons/NoPU/SingleElectron_DIGI_7.root',
    #'/store/group/comm_trigger/L1TrackTrigger/620_SLHC10/Extended2023TTI/Electrons/NoPU/SingleElectron_DIGI_8.root',
    #'/store/group/comm_trigger/L1TrackTrigger/620_SLHC10/Extended2023TTI/Electrons/NoPU/SingleElectron_DIGI_9.root',
    #'/store/group/comm_trigger/L1TrackTrigger/620_SLHC10/Extended2023TTI/Electrons/NoPU/SingleElectron_DIGI_10.root',
    )
process.source = cms.Source("PoolSource", fileNames = Source_Files)

#process.TFileService = cms.Service("TFileService", fileName = cms.string('SingleMuon_noPU_TrkPerf.root'), closeFileFast = cms.untracked.bool(True))
#process.TFileService = cms.Service("TFileService", fileName = cms.string('SingleMuon_PU140_Seed.root'), closeFileFast = cms.untracked.bool(True))
process.TFileService = cms.Service("TFileService", fileName = cms.string(name), closeFileFast = cms.untracked.bool(True))


############################################################
# Path definitions & schedule
############################################################

#run the tracking
#process.TTTracksFromPixelDigis.phiWindowSF = cms.untracked.double(2.0)
process.TTTracksFromPixelDigis.residuals = cms.untracked.bool(True)
process.TTTracksFromPixelDigis.ptPrecision = cms.untracked.double(0.5)

process.TT_step = cms.Path(process.TrackTriggerTTTracks)
process.TTAssociator_step = cms.Path(process.TrackTriggerAssociatorTracks)

# Define the track ntuple process, MyProcess is the (unsigned) PDGID corresponding to the process which is run
# e.g. single electron/positron = 11
#      single pion+/pion- = 211
#      single muon+/muon- = 13 
#      pions in jets = 6
process.L1TrackNtuple = cms.EDAnalyzer('L1TrackNtupleMaker',
                                       MyProcess = cms.int32(13),
                                       DebugMode = cms.bool(False)
                                       )

process.ana = cms.Path(process.L1TrackNtuple)

process.schedule = cms.Schedule(process.TT_step,process.TTAssociator_step,process.ana)
#process.schedule = cms.Schedule(process.ana)

