import pytest
from ReportDataContracts import StateInfo, OccupationInfo, ReportSummaryData
from ReportReader.H1bRawFileReader import H1bRawFileReader

def testTransformDictsToReportSummaryData():

    stateCountDict = {}
    stateCountDict['CA'] = 10
    stateCountDict['DE'] = 5
    stateCountDict['FL'] = 5

    occCountDict = {}
    occCountDict['Engineer'] = 14
    occCountDict['Manager'] = 4
    occCountDict['Analyst'] = 2

    reader = H1bRawFileReader('dummyFilename')
    reportSummaryData = reader.GetSummaryDataFromCounts(stateCountDict, occCountDict)

    stateRelRates = [reportSummaryData.StateInfos[0].RelRate, reportSummaryData.StateInfos[1].RelRate, reportSummaryData.StateInfos[2].RelRate ]

    assert stateRelRates[0] == 0.50
    assert stateRelRates[1] == 0.25
    assert stateRelRates[2] == 0.25

    occRelRates = [reportSummaryData.OccupationInfos[0].RelRate, reportSummaryData.OccupationInfos[1].RelRate, reportSummaryData.OccupationInfos[2].RelRate ]
    occRelRates.sort()

    assert occRelRates[0] == 0.10
    assert occRelRates[1] == 0.20
    assert occRelRates[2] == 0.70

