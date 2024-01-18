# DNA -> RNA Transcription
from typing import Union

TRANSCRIPTION_MAPPING = {"A": "U", "C": "G", "T": "A", "G": "C"}
ALLOWED_NUC = TRANSCRIPTION_MAPPING.keys()


def transcribe(seq: str, reverse: bool = False) -> str:
    """
    Write a function that will transcribe (replace DNA sequence to RNA
    by replacing all 'T' to 'U') in an input sequence
    """
    if (seq == "") or (seq is None):
        raise ValueError(f"No sequence was given")
    final_seq = []
    for nucleotide in seq:
        if nucleotide not in ALLOWED_NUC:
            raise ValueError(f"{seq} is not a valid sequence.")
        # Get transcribed nucleotide
        final_seq.append(TRANSCRIPTION_MAPPING[nucleotide])
    final_seq = ''.join(final_seq)
    return final_seq


def reverse_transcribe(seq: str) -> str:
    """
    Write a function that will transcribe an input sequence and reverse
    the sequence
    """
    transcribed = transcribe(seq)
    # Reverse sequence
    final_seq = ''.join(reversed(transcribed))
    return final_seq
