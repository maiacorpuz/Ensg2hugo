# Ensg2hugo
`# installable git clone for working with .gtf file
`# log on to trgn.usc.edu server
`ssh trgn.usc.edu # enter home directory on TRGN server
`git clone http://ftp.ensembl.org/pub/release-75/gtf/homo_sapiens
`mkdir data
`mv Homo_sapiens.GRCh37.75.gtf.gz ~/data
`gunzip Homo_sapiens.GRCh37.75.gtf.gz #unzip file using gunzip command
`cd ..
`mkdir projects
`cd projects
`vim ensg2hugo.py
