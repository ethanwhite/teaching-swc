
from dna_analysis import get_gc_content

def test_get_gc_content_zero():
    assert get_gc_content('ATTATTAAA') == 0