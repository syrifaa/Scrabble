# Knuth Morris Pratt Algorithm
def kmp_match(text, pat):
    border = compute_border(pat)
    i = 0
    j = 0
    m = len(pat)
    n = len(text)

    while i < n:
        if text[i] == pat[j]:
            if j == m - 1:
                return i - m + 1
            i += 1
            j += 1
        elif j > 0:
            j = border[j - 1]
        else:
            i += 1
    return -1

def compute_border(pat):
    border = [0] * len(pat)
    border[0] = 0
    j = 0
    i = 1

    while i < len(pat):
        if pat[j] == pat[i]:
            border[i] = j + 1
            j += 1
            i += 1
        elif j > 0:
            j = border[j - 1]
        else:
            border[i] = 0
            i += 1
    return border