## A GPT-4 tokenizer from scratch -- matching tiktoken cl100k_base encoding

### Training example:

```python
tokenizer = RegexTokenizer()
tokenizer.train(text, 276, verbose=True)

valtext = "Many common characters, including numerals, punctuation, and other symbols, are unified within the standard and are not treated as specific to any given writing system. Unicode encodes thousands of emoji, with the continued development thereof conducted by the Consortium as a part of the standard.[4] Moreover, the widespread adoption of Unicode was in large part responsible for the initial popularization of emoji outside of Japan. Unicode is ultimately capable of encoding more than 1.1 million characters."
valtext2 = tokenizer.decode(tokenizer.encode(valtext))
print(valtext2 == valtext)
# True
```

1. Implements the basic BPE algorithm described here: https://en.wikipedia.org/wiki/Byte-pair_encoding for tokenizer training
2. Supports regex split of text before applying BPE, as introduced in GPT-2 here: https://github.com/openai/gpt-2/blob/master/src/encoder.py (GPT-4 regex)
3. gpt4_tokenizer.py matches tiktoken cl100k_base encoding/decoding


Support of tiktoken vocab was implemented here: https://github.com/karpathy/minbpe/blob/master/minbpe/gpt4.py#L29

Does not support special tokens (like '<|endoftext|>') yet.


