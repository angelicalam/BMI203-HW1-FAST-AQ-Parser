# write tests for parsers

from seqparser import (
        FastaParser,
        FastqParser)

import pytest


def test_freebie_parser_1():
    """
    This one is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert True # things after the assert are true statements


def test_freebie_parser_2():
    """
    This too is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert 1 != 2

        
def test_FastaParser():
    """
    Write your unit test for your FastaParser class here. You should generate
    an instance of your FastaParser class and assert that it properly reads in
    the example Fasta File.

    Some example of "good" test cases might be handling edge cases, like Fasta
    files that are blank or corrupted in some way. Two example Fasta files are
    provided in /tests/bad.fa and /tests/empty.fa
    """
    fasta = FastaParser("data/test.fa")
    # Check that get_record returns a generator with values (header, sequence)
    for header, sequence in fasta.get_record(open(fasta.filename)):
      assert header != not None
      assert sequence != None
    # Check that the first entry of the example fasta file is correctly read.
    header0, sequence0 = list(fasta)[0]
    assert header0 == 'seq0'
    assert sequence0 == 'TGATTGAATCTTTTGAGGGTCACGGCCCGGAAGCCAGAATTTCGGGGTCCTCTGTGGATATTAATCGAGCCCACACGGTGTGAGTTCAGCGGCCCCCGCA'

    # Test that badly-formatted fasta raises a ValueError
    # Empty lines not allowed, although most fasta parsers will allow them between entries
    with pytest.raises(ValueError) as excinfo:
        bad = FastaParser("bad.fa")
    # Test that empty fasta raises a ValueError
    with pytest.raises(ValueError) as excinfo:
        empty = FastaParser("blank.fa")


def test_FastaFormat():
    """
    Test to make sure that a fasta file is being read in if a fastq file is
    read, the first item is None
    """
    # Check that get_record returns (None, ...) for a fastq file
    fastq = FastaParser("data/test.fq")
    header, sequence = next(fastq.get_record(open(fastq.filename)))
    assert header is None


def test_FastqParser():
    """
    Write your unit test for your FastqParser class here. You should generate
    an instance of your FastqParser class and assert that it properly reads 
    in the example Fastq File.
    """
    fastq = FastqParser("data/test.fq")
    # Check that get_record returns a generator with values (header, sequence)
    for header, sequence, quality in fastq.get_record(open(fastq.filename)):  
      assert header != None
      assert sequence != None
      assert quality != None
    # Check that the first entry of the example fastq file is correctly read.
    header0, sequence0, quality0 = list(fasta)[0]   
    assert header0 == 'seq0'
    assert sequence0 == 'TGTGGTCGTATAGTTATTGTCATAAATTACACAGAATCGCGATTCTCCGCGTCCACCAATCTTAGTGCACCACAGCATCGACCCGATTTATGACGCTGAG'
    assert quality0 == """*540($=*,=.062565,2>'487')!:&&6=,6,*7>:&132&83*8(58&59>'8!;28<94,0*;*.94**:9+7"94(>7='(!5"2/!%"4#32="""

    # Test that badly-formatted fastq raises a ValueError
    with pytest.raises(ValueError) as excinfo:
        bad = FastqParser("bad.fq")
    # Test that empty fastq raises a ValueError
    with pytest.raises(ValueError) as excinfo:
        empty = FastqParser("blank.fq")



def test_FastqFormat():
    """
    Test to make sure fastq file is being read in. If this is a fasta file, the
    first line is None
    """
    # Check that get_record returns (None, ...) for a fasta file
    fasta = FastqParser("data/test.fa")
    header, sequence, quality = next(fasta.get_record(open(fasta.filename)))
    assert header is None
