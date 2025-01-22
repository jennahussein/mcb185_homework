gunzip -c ~/Code/MCB185/data/D.melanogaster.gff.gz|cut -f 7|sort|uniq -c

gunzip -c ~/Code/MCB185/data/GCF_000005845.2_ASM584v2_protein.faa.gz|cut -f 4| grep -c "transporter"  

gunzip -c ~/Code/MCB185/data/GCF_000005845.2_ASM584v2_protein.faa.gz|cut -f 4| grep -c "reductase"    
              