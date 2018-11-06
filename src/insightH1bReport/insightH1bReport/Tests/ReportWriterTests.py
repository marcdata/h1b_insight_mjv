import pytest
from ReportDataContracts import StateInfo, OccupationInfo, ReportSummaryData
from ReportWriter import ReportWriter
from ReportWriter import ToReportPercentFormat

def testPercentFormat():
    relRate = 0.204
    assert ToReportPercentFormat(relRate) == '20.4%'

def testPercentFormatRoundDown():
    relRate = 0.0104
    assert ToReportPercentFormat(relRate) == '1.0%'

def testPercentFormatRoundUp():
    relRate = 0.0106
    assert ToReportPercentFormat(relRate) == '1.1%'

def testPercentFormatterRaisesOnBadinput():
    badRelRate = '0.123'
    with pytest.raises(ValueError):
        ToReportPercentFormat(badRelRate)

"""
report line format issues
"""

def testSampleStateReportLineFormat():
    stateInfo = StateInfo('KS', 10, 0.0501)
    reportWriter = ReportWriter()
    sampleOutput = reportWriter.ToReportLineState(stateInfo)
    assert sampleOutput == "KS;10;5.0%"

def testSampleOccupationReportLineFormat():
    occupationInfo = OccupationInfo('Data Engineer', 21, .1151)
    reportWriter = ReportWriter()
    sampleOutput = reportWriter.ToReportLineOccupation(occupationInfo)
    assert sampleOutput == "Data Engineer;21;11.5%"

