# pepeai-testnet
- experimental testnet for decentralized p2p AI processing



Setting up the environment:

```
conda install pytorch pytorch-cuda=11.7 -c pytorch -c nvidia
pip install -r requirements.txt
```

Running a Node:

PepeAI net seperates processing by PepeCoin Nodes.  Each node requires at least 1 GPU w/ 8GB+ or more of memory.

- bloom model layers distrubuted across fleet of pepecoin nodes
- will support various models as they are updated for pepecoin ai net


Start GPU Processing Node:
- ensure environment is setup as indicated above

```
python -m petals.cli.run_server bigscience/bloom-petals --initial_peers /ip4/54.164.52.79/tcp/8989/p2p/QmR7G6GZzeQeJoXfTovp8PJdJ7qxKYFwXUa2fp9p6BYdDi
```

Demo Chatbot:
```
python3 ./pepeaichatbot.py
```

