
# test_sample.py

import sample

def test_inc():
    assert sample.inc(3) == 4

def test_toCap():
    assert sample.toCap("aBcDeF") == "ABCDEF"
    assert sample.toCap("abCdeF") == "ABCDEF"