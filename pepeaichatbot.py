from petals import DistributedBloomForCausalLM
from transformers import AutoModelForCausalLM, AutoTokenizer

initial_peers = ['/ip4/54.164.52.79/tcp/8989/p2p/QmR7G6GZzeQeJoXfTovp8PJdJ7qxKYFwXUa2fp9p6BYdDi']

model = DistributedBloomForCausalLM.from_pretrained("bigscience/bloom-petals", tuning_mode="deep_ptune", pre_seq_len=16, initial_peers=initial_peers)


tokenizer = AutoTokenizer.from_pretrained("bigscience/bloom-petals")

# streaming chat bot
with model.inference_session(max_length=512) as sess:
    while True:
        prompt = input('Human: ')
        if prompt == "":
            break
        prefix = f"Human: {prompt}\nPepeAI:"
        prefix = tokenizer(prefix, return_tensors="pt")["input_ids"]
        print("PepeAI:", end="", flush=True)
        
        while True:
            outputs = model.generate(
                prefix, max_new_tokens=1, do_sample=True, top_p=0.9, temperature=0.75, session=sess
            )
            outputs = tokenizer.decode(outputs[0, -1:])
            print(outputs, end="", flush=True)
            if "\n" in outputs:
                break
            prefix = None  # Prefix is passed only for the 1st token of the bot's response

