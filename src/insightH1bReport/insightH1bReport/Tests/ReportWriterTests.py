import pytest
from ReportDataContracts import StateInfo, OccupationInfo, ReportSummaryData
from ReportWriter import ReportWriter
from ReportWriter import ToReportPercentFormat

def test_percent_format():
    relRate = 0.204
    assert ToReportPercentFormat(relRate) == '20.4%'

def test_percent_format_round_down():
    relRate = 0.0104
    assert ToReportPercentFormat(relRate) == '1.0%'

def test_percent_format_round_up():
    relRate = 0.0106
    assert ToReportPercentFormat(relRate) == '1.1%'

def test_percent_formatter_raises_on_badinput():
    badRelRate = '0.123'
    with pytest.raises(ValueError):
        ToReportPercentFormat(badRelRate)

"""
report line format issues
"""

def test_sample_state_report_line_format():
    stateInfo = StateInfo('KS', 10, 0.0501)
    reportWriter = ReportWriter()
    sampleOutput = reportWriter.ToReportLineState(stateInfo)
    assert sampleOutput == "KS;10;5.0%"

def test_sample_occupation_report_line_format():
    occupationInfo = OccupationInfo('Data Engineer', 21, .1151)
    reportWriter = ReportWriter()
    sampleOutput = reportWriter.ToReportLineOccupation(occupationInfo)
    assert sampleOutput == "Data Engineer;21;11.5%"

