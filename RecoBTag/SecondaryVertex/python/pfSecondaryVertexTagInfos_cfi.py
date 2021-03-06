import FWCore.ParameterSet.Config as cms

from RecoBTag.SecondaryVertex.vertexTrackSelection_cff import *
from RecoBTag.SecondaryVertex.vertexReco_cff import *
from RecoBTag.SecondaryVertex.vertexCuts_cff import *
from RecoBTag.SecondaryVertex.vertexSelection_cff import *

pfSecondaryVertexTagInfos = cms.EDProducer("CandSecondaryVertexProducer",
	vertexTrackSelectionBlock,
	vertexSelectionBlock,
	vertexCutsBlock,
	vertexRecoBlock,
	constraint = cms.string("BeamSpot"),
	trackIPTagInfos = cms.InputTag("pfImpactParameterTagInfos"),
	minimumTrackWeight = cms.double(0.5),
	usePVError = cms.bool(True),
	trackSort = cms.string('sip3dSig'),
        beamSpotTag = cms.InputTag('offlineBeamSpot'),                                        
        useExternalSV       = cms.bool(False),
        extSVCollection     = cms.InputTag('secondaryVertices'),
        extSVDeltaRToJet    = cms.double(0.3)
)
