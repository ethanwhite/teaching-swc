
"""Code for analyzing DNA sequences"""

from __future__ import division

def get_gc_content(seq):
    """Determine the GC content of a sequence"""
    seq = seq.replace('\n', '').replace(' ', '').upper()
    gc_content = 100 * (seq.count('G') + seq.count('C')) / len(seq)
    return gc_content