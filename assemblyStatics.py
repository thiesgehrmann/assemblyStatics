#!/usr/bin/python
################################################################################
#
# Wenchaolin, 2015 @ Tianjin Biochip
# linwenchao@yeah.net
#
################################################################################

import FastaUtils
import argparse

def run(fin):
    '''
    
    '''

    largestScaffoldName = ''
    largestScaffoldLength = 0
    countOfLargeSequence = 0
    totalGC = 0
    largeGC = 0
    lengthOfLargeSequence = 0
    countOfNs = 0
    allLenList = []
    largeLenList = []
    largeN = 0
    totalN = 0
    
    obj = FastaUtils.load(fin)
    
    for fa in obj:

        name = fa.name
        length = fa.length
        seq = fa.seq
        if fa.length > largestScaffoldLength:
            largestScaffoldName = name
            largestScaffoldLength = length
        if fa.isLarge:
            largeLenList.append(length)
            largeGC += seq.count('G') + seq.count('g')+ seq.count('c')+ seq.count('C')
            largeN += seq.count('N') + seq.count('n')
            
        lengthOfLargeSequence = sum(largeLenList)
        countOfLargeSequence = len(largeLenList)
        allLenList.append(length)
        totalGC += seq.count('G') + seq.count('g')+ seq.count('c')+ seq.count('C')
        totalN += seq.count('N') + seq.count('n')
        
    totalLength = sum(allLenList)
    totalCount = len(allLenList)
        
    print '\nAll sequences summary:'
    print '-----------------------'
    say('Counts of all sequences', totalCount)
    say('Length of all sequences', sum(allLenList))
    say('Largest scaffold name', largestScaffoldName)    
    say('Largest scaffold length', largestScaffoldLength)    
    say('All N50', FastaUtils.Nx0(allLenList, 50)[0])
    say('Counts of N50', FastaUtils.Nx0(allLenList, 50)[1])
    say('All N90', FastaUtils.Nx0(allLenList, 90)[0])
    say('Counts of N90', FastaUtils.Nx0(allLenList, 90)[1])
    sayPercent('GC content(%)', float(totalGC) / lengthOfLargeSequence * 100)
    sayPercent('N content (%)', float(totalN) / lengthOfLargeSequence * 100)
    
    
    print '\nLARGE (>1000bp) sequences summary:'
    print '-----------------------------------'
    say('Counts of LARGE sequences', countOfLargeSequence)
    say('Length of LARGE sequences', lengthOfLargeSequence)
    say('LARGE N50', FastaUtils.Nx0(largeLenList, 50)[0])
    say('Counts of LARGE N50', FastaUtils.Nx0(largeLenList, 50)[1])
    say('LARGE N90', FastaUtils.Nx0(largeLenList, 90)[0])
    say('Counts of LARGE N90', FastaUtils.Nx0(largeLenList, 90)[1])
    sayPercent('GC content(%)', float(largeGC) / lengthOfLargeSequence * 100)
    sayPercent('N content (%)', float(largeN) / lengthOfLargeSequence * 100)
    


def say(notes, value):
    '''format output'''
    
    print '%30s:\t%s' % (notes, value)
    return 1

def sayPercent(notes, value):
    '''Percent format output'''
    
    print '%30s:\t%.5s%%' % (notes, value)
    return 1
    
    
def parseArgs():
    '''
    parse options
    '''
    desc = 'A script to calculate a basic set of metrics from a genome assembly'
    parser = argparse.ArgumentParser(desc)
    parser.add_argument('-f', '--fasta', metavar = 'FASTA',
                        help = 'input fasta format file',
                        )
    args = parser.parse_args()
    return args

if __name__ == '__main__':
    
    args = parseArgs()
    
    try:
        fastaname = args.fasta
        f = open(fastaname, 'r')
        run(f)
    except:
        pass