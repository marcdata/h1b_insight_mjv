import sys

from ReportDataContracts import StateInfo, OccupationInfo, ReportSummaryData
from ReportWriter import ReportWriter
from ReportReader.H1bRawFileReader import H1bRawFileReader

def main(argv):
    inputfile = ''
    occupationsOutfile = ''
    statesOutfile = ''

    args = sys.argv
    if args[1] == '-h':
        print('usage: reportrunner.py <inputfile>  <occupationsoutputfile> <statessoutputfile>')
        sys.exit()
    if(len(args) != 4):
        print('usage: reportrunner.py <inputfile>  <occupationsoutputfile> <statessoutputfile>')
        sys.exit()

    inputfile = args[1]
    occupationsOutfile = args[2]
    statesOutfile = args[3]

    print('Input file is: ', inputfile)
    print('Occupations output file is: ', occupationsOutfile)
    print('States output file is: ', statesOutfile)

    RunReport(inputfile, occupationsOutfile, statesOutfile)

def RunReport(h1bRawDataFilename, occupationsOutfile, statesOutfile):
    """
    Run the report; read from the semicolon separated file, and write the output files.
    """

    # read from file into a summary data object
    reportSummaryData = H1bRawFileReader(h1bRawDataFilename).GetSummaryData()

    reportWriter = ReportWriter()
    reportWriter.WriteReportsToTargetFiles(reportSummaryData, occupationsOutfile, statesOutfile)

    return

if __name__ == "__main__":
    main(sys.argv[1:])