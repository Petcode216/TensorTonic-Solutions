import numpy as np

def pad_sequences(seqs: list, pad_value: int = 0, max_len: int | None = None) -> np.ndarray:
    """
    Returns: np.ndarray of shape (N, L) where:
      N = len(seqs)
      L = max_len if provided else max(len(seq) for seq in seqs) or 0
    """
    # Your code here
    if not seqs:
        return np.array([], dtype=int).reshape(0, 0)

    if max_len == None:
        L = max((len(s) for s in seqs), default=0)
    else:
        L = max_len

    padded = []

    for s in seqs:
        s = list(s[:L]) #Truncate if s > max_len
        padding = L - len(s)
        new_s = s + [pad_value] * padding
        padded.append(new_s)

    return np.array(padded, dtype=int)



 


            

    