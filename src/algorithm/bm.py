# Boyer Moore Algorithm
def bm_match(text, pattern):
    last = build_last(pattern)
    n = len(text)
    m = len(pattern)
    i = m - 1
    
    if i > n - 1:
        return -1  # no match if pattern is longer than text
    
    j = m - 1
    
    while i <= n - 1:
        if pattern[j] == text[i]:
            if j == 0:
                return i  # match
            else:
                i -= 1
                j -= 1
        else:
            lo = last[ord(text[i])]  # last occurrence
            i = i + m - min(j, 1 + lo)
            j = m - 1
    
    return -1  # no match

def build_last(pattern):
    last = [-1] * 128  # ASCII char set
    for i in range(len(pattern)):
        last[ord(pattern[i])] = i
    return last