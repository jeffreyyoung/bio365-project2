import sys
from kmer_frequency import remove_mis_reads
from stats import printStats

def get_reads_from_fasta(fastaFileName):
    with open(fastaFileName) as fh:
        seq = ''
        reads = []
        for line in fh:
            if line[0] == '>':
                seq_header = line.strip()
            else:
                reads.append(line.strip())
        return reads

def get_kmers(text, k):
    kmers = []
    for i in range( len(text) - k + 1 ):
        kmers.append(text[i:i+k])
    return kmers;

def get_kmers_from_fasta(k):
    reads = get_reads_from_fasta(sys.argv[1])
    kmers = []
    for r in reads:
        kmers += get_kmers(r, k)
    return kmers;

k = int(sys.argv[2])
all_kmers = get_kmers_from_fasta(k)

#remove outlier kmers
kmers = set(remove_mis_reads( all_kmers ))
#kmers = set( all_kmers )
##### below is stanley's code #######
g = dict()
counts = dict()
edge_count = 0

for kmer in kmers:
    left = kmer[ : -1 ]
    right = kmer[ 1 : ]
    edge_count += 1

    if left in g:
        g[ left ].append( right )
    else:
        g[ left ] = [ right ]

    if left in counts:
        counts[ left ][ 1 ] += 1
    else:
        counts[ left ] = [ 0, 1 ]

    if right in counts:
        counts[ right ][ 0 ] += 1
    else:
        counts[ right ] =[ 1, 0 ]

non_branching = set()
contigs = []

def build_graph( start, g ):
    global edge_count
    path = [ start ]
    cur_node = start

    while len( cur_node ) > 0:
        next_node = g[ cur_node ][ 0 ]
        del g[ cur_node ][ 0 ]
        #if len( g[ cur_node ] ) == 0:
        #    del g[ cur_node ]
        edge_count -= 1

        if next_node in non_branching:
            path.append( next_node )
            cur_node = next_node
            continue
        else:
            path.append( next_node )
            break

    return path

def merge_nodes( nodes ):
    contig = nodes[ 0 ]
    for i in range( 1, len( nodes ) ):
        contig += nodes[ i ][ -1 ]
    return contig

def has_outgoing( node ):
    if len( g[ node ] ) > 0:
        return True
    else:
        return False

for key, item in counts.iteritems():
    if item[ 0 ] == 1 and item[ 1 ] == 1:
        non_branching.add( key )

start = g.keys()[ 0 ]

while edge_count > 0:
    for i in g.keys():
        if i in non_branching or len( g[ i ] ) == 0:
            continue
        start = i
        break
    c = build_graph( start, g )
    contigs.append( c )

result = [merge_nodes(contig) for contig in contigs]
for r in result:
    print r

printStats(result)
