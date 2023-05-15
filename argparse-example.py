
#example for handling options of cleaning script


import argparse 
import os.path
import sys

####
#Read in command line options and check files exist
####

parser = argparse.ArgumentParser(description = 'Process list of restriction enzymes to retreive coordinates from reference genome')

parser.add_argument('-b', '--bamfile', metavar = 'bam file', required = True, dest = 'bamfile', action='store', help = 'File of reads aligned to reference genome in BAM format')
parser.add_argument('-e', '--enzymefile', metavar = 'enzyme file', required = True, dest = 'enzymefile', action='store', help='Tab-delimited text file of enzyme names and sequences')
parser.add_argument('-r', '--referencegenome', metavar = 'reference genome', required = True, dest = 'referencegenome', action='store', help='FASTA file of reference genome contigs')

args = parser.parse_args()

#confirm behavior of how argparse store variables
#print(args.bamfile)
#print(args.enzymefile)
#print(args.referencegenome)

#test behavior of os.path
#print(os.path.isfile(args.bamfile))
#print(os.path.isfile(args.enzymefile))
#print(os.path.isfile(args.referencegenome))


if (os.path.isfile(args.bamfile) == True and os.path.isfile(args.enzymefile) == True and os.path.isfile(args.referencegenome) == True):
    print('all files found')
else:
    if (os.path.isfile(args.bamfile) == False):
        print('bam file was not found')
    if (os.path.isfile(args.enzymefile) == False):
        print('enzyme file  was not found')
    if (os.path.isfile(args.referencegenome) == False):
        print('reference genome fasta file  was not found')   
    sys.exit('exiting due to missing arguements')
	
