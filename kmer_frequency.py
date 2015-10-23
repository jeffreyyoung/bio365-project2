#paul is doing this

thresholdPercent = .1; #this value is a percent of the average frequency
# to be used as a threshold for determining which kmers are likely misreads


def getFrequencyAverage(freqDict):
    total = 0.0;
    for key in freqDict:
        total += freqDict[key];

    total /= len(freqDict);
    return total;

def remove_mis_reads(kmers):
    #ACG
    #ACG
    #TTA

    #get frequency of each kmer
    freqDict = {}
    for kmer in kmers:
        if kmer in freqDict:
            freqDict[kmer] += 1;
        else:
            freqDict[kmer] = 1;
    #remove kmers with low frequency
    #print (freqDict);
    average = getFrequencyAverage(freqDict);
    #print (average);
    threshold = average * thresholdPercent;
    toRemove = [];
    for key in freqDict:
        if freqDict[key] < threshold:
            toRemove.append(key);
            #removeAllOfKmer(freqDict[key]);
    remainingKmers = [x for x in kmers if x not in toRemove]
    #example... if average kmer frequency is 20, remove kmers with frequency less than 4
    return remainingKmers;



# #'''
# #FOR TESTING
# testKmers = [
#  "ATTG",
#  "ATTG",
#  "CCCG",
#  "CGGC",
#  "AGCC",
#  "ACCG",
#  "ATCG",
#  "ATTG",
#  "CGGC",
#  "ATTG",
#  "ATTG",
#  "ATTG",
#  "CGGC",
#  "AGCC",
#  "ACCG",
#  "ATCG",
#  "ATTG",
#  "CGGC",
#  "ATTG",
#  "ATTG",
#  "TGCC",
#  "CGGC",
#  "AGCC",
#  "ACCG",
#  "ATCG",
#  "ATTG",
#  "CGGC",
#  "ATTG",
#  "ATTG",
#  "ATTG",
#  "CGGC",
#  "AGCC",
#  "ACCG",
#  "ATCG",
#  "ATTG",
#  "CGGC"
# ];
#
# testKmers = remove_mis_reads(testKmers);
# print("remaining Kmers");
# print(testKmers);
# #'''
