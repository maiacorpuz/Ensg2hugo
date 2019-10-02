# Ensg2hugo
# installable git clone for working with .gtf file
Hello there! To begin, log on to **trgn.usc.edu server.**

Now that you're in the home directory on TRGN, execute the following: 

git clone http://ftp.ensembl.org/pub/release-75/gtf/homo_sapiens

You'll need to move the .gtf file to a new directory before moving further.

To do so,

mkdir data

_Since you're still in the home directory you can execute the following to move the .gtf file:_

mv Homo_sapiens.GRCh37.75.gtf.gz ~/data

**Now** let's unzip the file to make all data available to read.

_Execute:_

gunzip Homo_sapiens.GRCh37.75.gtf.gz #unzip file using gunzip command

_This should allow you to work to and from the .gtf file now. You may create a separate directory to create a program for running a "search and replace" command of python to modify the .gtf file._

cd ..

mkdir projects

cd projects

vim ensg2hugo.py

_You may find the executable program as a file named Ensg2hugo.py listed above in this repository._
