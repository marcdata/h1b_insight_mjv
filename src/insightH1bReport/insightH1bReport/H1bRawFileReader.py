from ReportDataContracts import ReportSummaryData, StateInfo, OccupationInfo
from RowExtractor import RowExtractor, SlimRow
from RowExtractor import BuildRowExtractorFromHeaderRow

class H1bRawFileReader(object):
    """
    Responsible for reading raw data from semicolon separated files.

    """


    def __init__(self, filename):
        """
        Where filename is the semicolon-separated-value formatted data input file.
        """
        self.filename = filename

    def GetSummaryData(self):
        """
        Read the data file, and accumulate counts. 
        
        Returns ReportSummaryData object, which has data by state, and by occupation.
        """
        stateCountDict = {}
        occupationCountDict = {}

        with open(self.filename, 'r') as inputFile:
            line = inputFile.readline()

            # headerRow = line
            #headerRowParts = headerRow.split(';')
            #caseStatusCol = headerRowParts.index('CASE_STATUS')
            #stateCol = headerRowParts.index('WORKSITE_STATE')
            #occupationDescCol = headerRowParts.index('SOC_NAME')

            rowExtractor = BuildRowExtractorFromHeaderRow(line)

            for line in inputFile:
                #line = inputFile.readline()
                slimRow = rowExtractor.GetSlimRow(line)

                # filter operation
                if(slimRow.CertStatus.upper() != 'CERTIFIED'):
                    continue

                if(slimRow.State not in stateCountDict.keys()):
                    stateCountDict[slimRow.State] = 0
                stateCountDict[slimRow.State] += 1

                if(slimRow.Occupation not in occupationCountDict.keys()):
                    occupationCountDict[slimRow.Occupation] = 0
                occupationCountDict[slimRow.Occupation] += 1

                #line = inputFile.readline()

        return self.GetSummaryDataFromCounts(stateCountDict, occupationCountDict)

    def GetSummaryDataFromCounts(self, stateCountDict, occupationCountDict):
        """
        Convert raw dictionary counts into data for rest of the report. 
        Supplement raw counts with relative rate data.

        This handles the portion of the data transform that is contingent on aggregate values.
        """
        totalCertCount = sum(stateCountDict.values())
        altTotalCertCount = sum(occupationCountDict.values())
        if(totalCertCount != altTotalCertCount):
            raise(ValueError('Data inconsistent, total counts do not match.'))
        if(totalCertCount == 0):
            raise(ValueError('Zero total count. This will cause problems (divide by zero).'))

        reportSummaryData = ReportSummaryData()
        for stateKey in stateCountDict.keys():
            count = stateCountDict[stateKey]
            relRate = float(count) / totalCertCount
            reportSummaryData.StateInfos.append(StateInfo(stateKey, count, relRate))

        for occupationKey in occupationCountDict.keys():
            count = occupationCountDict[occupationKey]
            relRate = float(count) / totalCertCount
            reportSummaryData.OccupationInfos.append(OccupationInfo(occupationKey, count, relRate))

        return reportSummaryData



