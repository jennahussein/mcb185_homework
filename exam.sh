gunzip -c ~/Code/MCB185/data/D.melanogaster.gff.gz|cut -f 7|sort|uniq -c
more genes on the negative strand (1856)

gunzip -c ~/Code/MCB185/data/GCF_000005845.2_ASM584v2_protein.faa.gz|cut -f 4| grep -c "transporter"  
289
gunzip -c ~/Code/MCB185/data/GCF_000005845.2_ASM584v2_protein.faa.gz|cut -f 4| grep -c "reductase"    
177              