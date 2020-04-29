#!/usr/bin/env python3
from pl_curve import run
import pandas
import os

def test_if_file_exists():
    assert os.path.isfile("test.tsv") is True
    assert os.path.isfile("test.png") is True

def test_run():

    f = open("test-input.tsv", "w")
    f.write("Bin\tStep I\tStep II\n")
    f.write("219\t0.5\t0.3\n")
    f.write("218\t0.5\t0.7\n")
    f.close()

    # delete test.png, we know it exists because of the function test_if_file_exists()
    os.remove("test.tsv")

    # delete test.png, we know it exists because of the function test_if_file_exists()
    os.remove("test.png")

    run("test-input.tsv", "test.png", "test.tsv")
    assert os.path.isfile("test.tsv") is True
    assert os.path.isfile("test.png") is True

    data = pandas.read_csv("test.tsv", delimiter='\t', index_col=0)
    assert data.loc['Step I', 'Gini'] == 0.0
    assert data.loc['Step I', 'Corrected Gini'] == 0.0
    assert data.loc['Step II', 'Gini'] == 0.2
    assert data.loc['Step II', 'Corrected Gini'] == 0.4
