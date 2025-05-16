# a test file for globber.py
import pytest

def artifact():
    return "artifact"

def test_artifact():    
    assert artifact() == "artifact"
