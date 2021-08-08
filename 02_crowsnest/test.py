#!/usr/bin/env python3
"""tests for crowsnest.py"""

import os
from subprocess import getstatusoutput, getoutput

prg = './crowsnest.py'
consonant_words = [
    'brigantine', 'clipper', 'dreadnought', 'frigate', 'galleon', 'haddock',
    'junk', 'ketch', 'longboat', 'mullet', 'narwhal', 'porpoise', 'quay',
    'regatta', 'submarine', 'tanker', 'vessel', 'whale', 'xebec', 'yatch',
    'zebrafish'
]
vowel_words = ['aviso', 'eel', 'iceberg', 'octopus', 'upbound']
invalid_inputs = ['1aga', '^ada']
template = 'Ahoy, Captain, {} {} off the larboard bow!'


# --------------------------------------------------
def test_exists():
    """exists"""

    assert os.path.isfile(prg)


# --------------------------------------------------
def test_usage():
    """usage"""

    for flag in ['-h', '--help']:
        rv, out = getstatusoutput(f'{prg} {flag}')
        assert rv == 0
        assert out.lower().startswith('usage')


# --------------------------------------------------
def test_consonant():
    """brigantine -> a brigantine"""

    for word in consonant_words:
        out = getoutput(f'{prg} {word}')
        assert out.strip() == template.format('a', word)


# --------------------------------------------------
def test_consonant_upper():
    """brigantine -> a Brigatine"""

    for word in consonant_words:
        out = getoutput(f'{prg} {word.title()}')
        assert out.strip() == template.format('A', word.title())


# --------------------------------------------------
def test_vowel():
    """octopus -> an octopus"""

    for word in vowel_words:
        out = getoutput(f'{prg} {word}')
        assert out.strip() == template.format('an', word)


# --------------------------------------------------
def test_vowel_upper():
    """octopus -> an Octopus"""

    for word in vowel_words:
        out = getoutput(f'{prg} {word.upper()}')
        assert out.strip() == template.format('An', word.upper())

# --------------------------------------------------
def test_case_match():
    """
    an octopus
    An Octopus
    a whale
    A Whale
    """

    for word in vowel_words:
        out = getoutput(f'{prg} {word.upper()}')
        assert out.strip() == template.format('An', word.upper())
        out = getoutput(f'{prg} {word}')
        assert out.strip() == template.format('an', word)

    for word in consonant_words:
        out = getoutput(f'{prg} {word.upper()}')
        assert out.strip() == template.format('A', word.upper())
        out = getoutput(f'{prg} {word}')
        assert out.strip() == template.format('a', word)

# --------------------------------------------------
def test_side():
    """larboard and starboard"""

    optional_param_side = '--side starboard'
    for word in vowel_words:
        out = getoutput(f'{prg} {word} {optional_param_side}')
        assert out.strip() == template.format('an', word).replace('larboard', 'starboard')

# --------------------------------------------------
def test_inavlid_object():
    """input starting with number or special character"""

    for word in invalid_inputs:
        out = getoutput(f'{prg} {word}')
        assert "ValueError" in out.strip()
        assert 'should start with an alphabet' in out.strip()
