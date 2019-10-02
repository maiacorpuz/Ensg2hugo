# Ensg2hugo
# installable git clone for working with .gtf file
Hello there! To begin, log on to trgn.usc.edu server.
Now that you're in the home directory on TRGN 
git clone http://ftp.ensembl.org/pub/release-75/gtf/homo_sapiens
mkdir data
mv Homo_sapiens.GRCh37.75.gtf.gz ~/data
gunzip Homo_sapiens.GRCh37.75.gtf.gz #unzip file using gunzip command
cd ..
mkdir projects
cd projects
vim ensg2hugo.py
