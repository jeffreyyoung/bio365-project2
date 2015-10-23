for fasta in real.error.large.fasta real.error.small.fasta synthetic.example.noerror.small.fasta synthetic.noerror.large.fasta synthetic.noerror.small.fasta
do
 python de_bruijn_assembler.py data-sets/$fasta 13 > data-sets-results/$fasta.output
done
