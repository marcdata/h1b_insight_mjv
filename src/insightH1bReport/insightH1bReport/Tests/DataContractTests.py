
from ReportDataContracts import *

def testDefaultInitialAmountStateInfo():
    stateInfo = StateInfo('TX')
    assert stateInfo.Count == 0
    assert stateInfo.RelRate == 0.0

def testDefaultInitialAmountOccupationInfo():
    occupationInfo = OccupationInfo('Teacher')
    assert occupationInfo.Count == 0
    assert occupationInfo.RelRate == 0.0

