# pepeai-testnet
- experimental testnet for decentralized p2p AI processing



Setting up the chatbot environment:

```
conda install pytorch pytorch-cuda=11.7 -c pytorch -c nvidia
pip install -r requirements.txt
python3 ./pepeaichatbot.py
```

Running a Node:

PepeAI net seperates processing by PepeCoin Nodes.  Each node requires at least 1 GPU w/ 8GB+ or more of memory.

- bloom model layers distrubuted across fleet of pepecoin nodes
- will support various models as they are updated for pepecoin ai net

