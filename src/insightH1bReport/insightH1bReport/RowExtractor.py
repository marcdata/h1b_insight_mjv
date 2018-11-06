class SlimRow(object):
    """
    Simple data contract, data transfer object.
    """
        
    def __init__(self, certStatus, stateCode, occupation):
        self.CertStatus = certStatus
        self.State = stateCode
        self.Occupation = occupation

class RowExtractor(object):
    """
    RowExtractor gets SlimRows objects from the raw report row.

    Handles extraction logic.
    """

    def __init__(self, certCol, stateCol, occupationCol):
        self.CertCol = certCol
        self.StateCol = stateCol
        self.OccupationCol = occupationCol

    def GetSlimRow(self, line):
        lineByParts = line.split(';')

        return SlimRow(lineByParts[self.CertCol], lineByParts[self.StateCol], lineByParts[self.OccupationCol])


# Pulled out from static class method to just a method.
def BuildRowExtractorFromHeaderRow(headerRow):
    headerRowParts = headerRow.split(';')
    caseStatusCol = headerRowParts.index('CASE_STATUS')
    stateCol = headerRowParts.index('WORKSITE_STATE')
    occupationCol = headerRowParts.index('SOC_NAME')

    rowExtractor = RowExtractor(caseStatusCol, stateCol, occupationCol)
    return rowExtractor
