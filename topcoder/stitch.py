"""
`Stitch <http://community.topcoder.com/stat?c=problem_statement&pm=3946>`__
"""

def solution (A, B, overlap):
    out = [None for _ in range(len(A))]
    for i in range(len(A)):
        if overlap == 0:
            out[i] = A[i] + B[i]
            continue
        head = A[i][:-overlap]
        a    = A[i][-overlap:]
        b    = B[i][:overlap]
        tail = B[i][overlap:]
        out[i] = head + overlay(a, b) + tail
    return out

def overlay (a, b):
    out = ""
    for i in range(1, len(a) + 1):
        x = float(ord(a[i-1]))
        y = float(ord(b[i-1]))
        z = round(((len(a) + 1 - i) * x + (i * y)) / (len(a) + 1), 0)
        out += chr(int(z))
    return out
