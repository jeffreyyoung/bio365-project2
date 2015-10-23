#real.error.large.fasta real.error.small.fasta synthetic.example.noerror.small.fasta synthetic.noerror.large.fasta synthetic.noerror.small.fasta
for fasta in real.error.large.fasta
do
  echo $fasta
  a=5

  while [ $a -lt 100 ]
  do
     echo $a
     python de_bruijn_assembler.py data-sets/$fasta $a > data-sets-results/$fasta.$a.output
     ((a+=1))
  done
  #python de_bruijn_assembler.py data-sets/$fasta 13 > data-sets-results/$fasta.output
done
