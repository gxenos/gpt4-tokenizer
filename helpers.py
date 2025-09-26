def get_stats(tokens):
    pairs = {}
    for pair in zip(tokens, tokens[1:]):
        pairs[pair] = pairs.get(pair, 0) + 1
    return pairs

def merge(tokens, pair, idx):
    updated_tokens = []
    (p1,p2) = pair

    j = 0
    while j < len(tokens):
        if j < len(tokens) - 1 and tokens[j] == p1 and tokens[j+1] == p2:
            updated_tokens.append(idx)
            j += 2
        else:
            updated_tokens.append(tokens[j])
            j += 1

    return updated_tokens