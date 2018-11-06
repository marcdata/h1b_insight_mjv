from ReportDataContracts import ReportSummaryData, StateInfo, OccupationInfo

class ReportWriter():
    """Responsible for writing summary data to target output."""

    StateHeaderLine = "TOP_STATES;NUMBER_CERTIFIED_APPLICATIONS;PERCENTAGE";
    OccupationHeaderLine = "TOP_OCCUPATIONS;NUMBER_CERTIFIED_APPLICATIONS;PERCENTAGE";

    def WriteReportsToTargetFiles(self, reportSummaryData, targetOccupationFilename, targetStateFilename, topN = 10):
        if(not isinstance(reportSummaryData, ReportSummaryData)):
            raise(TypeError('Not of type ReportSummaryData'))
        
        orderedOccupations = sorted(reportSummaryData.OccupationInfos, key = occupationOrderingFunc)[:topN]

        with open(targetOccupationFilename, 'w') as occupationFile:
            occupationFile.write(self.OccupationHeaderLine + '\n')
            for occupationInfo in orderedOccupations:
                occupationFile.write(self.ToReportLineOccupation(occupationInfo) + '\n')

        orderedStateInfos = sorted(reportSummaryData.StateInfos, key = stateOrderingFunc)[:topN]

        with open(targetStateFilename, 'w') as stateFile:
            stateFile.write(self.StateHeaderLine + '\n')
            for stateInfo in orderedStateInfos:
                stateFile.write(self.ToReportLineState(stateInfo) + '\n')
        return

    def WriteReportToConsole(self, reportSummaryData, topN = 10):
        if(not isinstance(reportSummaryData, ReportSummaryData)):
            raise(TypeError('Not of type ReportSummaryData'))
        if(topN < 0):
            raise(ValueError('topN parameter less than zero.'))

        orderedOccupations = sorted(reportSummaryData.OccupationInfos, key = occupationOrderingFunc)[:topN]

        print(self.OccupationHeaderLine)
        for occupationInfo in orderedOccupations:
            print(self.ToReportLineOccupation(occupationInfo))

        orderedStateInfos = sorted(reportSummaryData.StateInfos, key = stateOrderingFunc)[:topN]

        print('\n')
        print(self.StateHeaderLine)
        for stateInfo in orderedStateInfos:
            print(self.ToReportLineState(stateInfo))
        return

    def ToReportLineState(self, stateInfo):
        return "{st};{ct};{relRate}".format(st = stateInfo.State, ct = stateInfo.Count, relRate = ToReportPercentFormat(stateInfo.RelRate))

    def ToReportLineOccupation(self, occupationInfo):
        return "{jobDesc};{ct};{relRate}".format(jobDesc = occupationInfo.OccupationDescription, ct = occupationInfo.Count, relRate = ToReportPercentFormat(occupationInfo.RelRate))

def ToReportPercentFormat(relRate):
    if(not isinstance(relRate, float)):
        raise(ValueError('relRate should be a float'))
    return "{:.1%}".format(relRate)

def occupationOrderingFunc(occupationInfo):
    return (-occupationInfo.Count, occupationInfo.OccupationDescription)

def stateOrderingFunc(stateInfo):
    return (-stateInfo.Count, stateInfo.State)


