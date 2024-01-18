# write tests for transcribe functions

from seqparser import (
        transcribe,
        reverse_transcribe)


def test_freebie_transcribe_1():
    """
    This one is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert True


def test_freebie_transcribe_2():
    """
    This too is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert 1 != 2

        
def test_transcribe():
    """
    Write your unit test for the transcribe function here.
    """
    # Check that transcribe raises a ValueError if an invalid sequence is given
    # Ambiguous bases are not accepted
    with pytest.raises(ValueError) as excinfo:
        bad = transcribe('AGX!TC')
    # Check that transcribe raises a ValueError if no sequence is given
    with pytest.raises(ValueError) as excinfo:
        blank = transcribe(None)
    # Check that transcribe performs as expected with a validated example
    assert transcribe('ACTGAACCC') == 'UGACUUGGG' 


def test_reverse_transcribe():
    """
    Write your unit test for the reverse transcribe function here.
    """
    # Check that reverse_transcribe raises a ValueError if an invalid sequence is given
    # Ambiguous bases are not accepted
    with pytest.raises(ValueError) as excinfo:
        bad = reverse_transcribe('AGX!TC')
    # Check that reverse_transcribe raises a ValueError if no sequence is given
    with pytest.raises(ValueError) as excinfo:
        blank = reverse_transcribe(None)
    # Check that reverse_transcribe performs as expected with a validated example
    assert reverse_transcribe('ACTGAACCC') == 'GGGUUCAGU'
