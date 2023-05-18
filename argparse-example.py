
#example for handling options of cleaning script


import argparse 
import os.path
import sys

####
#Read in command line options and check files exist
####

parser = argparse.ArgumentParser(description = 'Process list of restriction enzymes to retreive coordinates from reference genome')

parser.add_argument('-b', '--bamfile', metavar = 'bam file', required = True, dest = 'bamfile', action='store', help = 'File of reads aligned to reference genome in BAM format')
parser.add_argument('-e', '--enzymefile', metavar = 'enzyme file', required = True, dest = 'enzymefile', action='store', help='Comma-delimited text file of enzyme names and sequences')
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
	
## Reworking the Perl script "PreprocessSAMs.pl" for the AllHiC pipeline
import subprocess
from subprocess import Popen
import pandas as pd

#check files exist (read command line options in)

#turn .txt file of enzymes into list
input_enzymes=pd.read_csv(args.enzymefile, sep=',')

#initialize final list of enzymes to turn into bed files
enzyme_list=[]


#if there is an uncertain base in the enzyme then cycle through the possible bases
for i in input_enzymes:
    if "N" in i:
        #add each possible enzyme to the enzyme list
        bases=["A","C","G","T"]
        for n in bases:
            x=i.replace("N", n)
            enzyme_list.append(x)
            

    #if no uncertain base append enzyme to list      
    else:
        enzyme_list.append(i)

print(enzyme_list)

#iterate through the enzyme list and run the perl script to generate the bed files
#create variables that hold the fasta file and the range as a string (if int the perl script fails)
fasta = args.referencegenome
range = "500"
for j in enzyme_list:
  subprocess.call(["perl", "make_bed_around_RE_site.pl", fasta, j, range])
