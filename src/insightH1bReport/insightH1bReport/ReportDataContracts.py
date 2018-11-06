

class ReportSummaryData:

    def __init__(self):
        self.StateInfos = []
        self.OccupationInfos = []

class StateInfo:
    def __init__(self, stateCode, count = 0, relRate = 0.0):
        self.State = stateCode
        self.Count = count
        self.RelRate = relRate

class OccupationInfo:
    def __init__(self, occupationDesc, count = 0, relRate = 0.0):
        self.OccupationDescription = occupationDesc
        self.Count = count
        self.RelRate = relRate

