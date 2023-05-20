# pepeai-testnet
- experimental testnet for decentralized p2p AI processing



Setting up the environment:

Nvidia Driver:
```
sudo apt-get update && sudo apt-get install nvidia-driver-530
```


Docker:
 - Linux
 - Windows
 - OSX

```
sudo docker run -p 31330:31330 --ipc host --gpus all --volume petals-cache:/cache --rm     learningathome/petals:main python -m petals.cli.run_server bigscience/bloomz-petals --initial_peers /ip4/54.164.52.79/tcp/8989/p2p/QmR7G6GZzeQeJoXfTovp8PJdJ7qxKYFwXUa2fp9p6BYdDi --port 31330
```

Or install manually:

Anaconda Install:

```
wget https://repo.anaconda.com/archive/Anaconda3-2023.03-1-Linux-x86_64.sh
chmod +x ./Anaconda3-2023.03-1-Linux-x86_64.sh
./Anaconda3-2023.03-1-Linux-x86_64.sh
```

Answer yes to base env setup.

```
conda create -n pepeaitestnet python=3.10
conda activate pepeaitestnet
conda install pytorch pytorch-cuda=11.7 -c pytorch -c nvidia
pip install -U petals
```

Running a Node:

PepeAI net seperates processing by PepeCoin Nodes.  Each node requires at least 1 GPU w/ 8GB+ or more of memory.

- bloom model layers distrubuted across fleet of pepecoin nodes
- will support various models as they are updated for pepecoin ai net


Start GPU Processing Node:
- ensure environment is setup as indicated above
- If you have more than 1 GPU, set the GPU index before starting the node
- you can run multiple nodes under screen
- optional IP:PORT for improved network performance, use --public_ip x.x.x.x --port 8989
- from linux cli, to get public ip
```
curl ifconfig.me
```

- Run Node (don't forget to add --port 8989 --public_ip x.x.x.x) if you have setup port forwarding on your router

```
export CUDA_VISIBLE_DEVICES=0  # Insert the GPU index here, counting from zero
python -m petals.cli.run_server bigscience/bloomz-petals --initial_peers /ip4/54.164.52.79/tcp/8989/p2p/QmR7G6GZzeQeJoXfTovp8PJdJ7qxKYFwXUa2fp9p6BYdDi
```

Demo Chatbot:
```
python3 ./pepeaichatbot.py
```

