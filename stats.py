__author__ = 'adam'

import numpy

def printStats( contigs ):
    #["", ""]
    contigsLen = []
    contigsLenPrime = []
    largestContigLen = 0
    for contig in contigs:
        contigsLen.append( len(contig))
        if( len(contig) > largestContigLen):
            largestContigLen = len(contig)
        for i in range(0, len(contig)):
            contigsLenPrime.append( len(contig) )
    n50 = numpy.median( numpy.array(contigsLenPrime) )
    avgContigSize = numpy.median( numpy.array(contigsLen) )
    contigCount = len(contigs)
    print "\n\n--------Stats-------------"
    print "Average Contig Size: " + str(avgContigSize)
    print "N50: " + str(n50)
    print "Number of Contigs:  " + str(contigCount)
    print "Largest Contig Size: " + str(largestContigLen)
