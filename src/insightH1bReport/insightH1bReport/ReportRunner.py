
import sys
import getopt

from ReportDataContracts import StateInfo, OccupationInfo, ReportSummaryData
from ReportWriter import ReportWriter
from ReportReader.H1bRawFileReader import H1bRawFileReader

def main(argv):
   inputfile = ''
   outputfile = ''
   try:
      opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
   except getopt.GetoptError:
      print('test.py -i <inputfile> -o <outputfile>')
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print('test.py -i <inputfile> -o <outputfile>')
         sys.exit()
      elif opt in ("-i", "--ifile"):
         inputfile = arg
      elif opt in ("-o", "--ofile"):
         outputfile = arg
   print('Input file is ', inputfile)
   print ('Output file is ', outputfile)

   #do_more()
   #do_more_occupations()
   #do_more_3()

   inputfile = r'C:\xprojects\insight-data\resampled\h1b_fy_2015_n20.csv'
   RunReport(inputfile)

#def do_more_3():
#    rsd = ReportSummaryData()
#    rsd.StateInfos.append(StateInfo('TX', 10, 0.021))
#    rsd.StateInfos.append(StateInfo('KS', 7, 0.018))
#    rsd.StateInfos.append(StateInfo('NE', 8, 0.019))

#    rsd.OccupationInfos.append(OccupationInfo('Data analyst', 5, 0.022))
#    rsd.OccupationInfos.append(OccupationInfo('Software developer', 15, 0.042))
#    rsd.OccupationInfos.append(OccupationInfo('Data scientist', 1, 0.012123))

#    reportWriter = ReportWriter()
#    reportWriter.WriteReportToConsole(rsd, topN = 5)

#    reportWriter.WriteReportsToTargetFiles(rsd, 'occupationOut.txt', 'stateOut.txt')

def RunReport(h1bRawDataFilename):

    # read from the semicolon separated file

    # do data file reader / GetSummaryData()
    reportSummaryData = H1bRawFileReader(h1bRawDataFilename).GetSummaryData()

    # target files
    targetOccupationOut = 'occupationOut.txt';
    targetStateOut = 'stateOut.txt'

    reportWriter = ReportWriter();
    reportWriter.WriteReportsToTargetFiles(reportSummaryData, 'occupationOut.txt', 'stateOut.txt')

    return

if __name__ == "__main__":
   main(sys.argv[1:])