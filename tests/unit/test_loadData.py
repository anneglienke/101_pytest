import pandas as pd
import pytest
import os

from src.main import loadData

## THIS SHOULD FAIL


# Fixture to provide a sample DataFrame for testing
@pytest.fixture
def sample_dataframe():
    data = {
        "customer_id": [5, 6, 10],
        "city": ["London", "Manchester", "San Francisco"],
        "country": ["UK", "UK", "USA"],
    }
    return pd.DataFrame(data)


# Fixture to create a temporary output directory for testing
@pytest.fixture
def temporary_output_dir(tmpdir):
    return tmpdir.mkdir("output")


# Test the loadData function
def test_loadData(sample_dataframe, temporary_output_dir):
    # Call the function under test
    loadData(sample_dataframe)

    # Assert that the output files are created in the temporary directory
    assert os.path.exists(temporary_output_dir.join("file1.csv"))
    assert os.path.exists(temporary_output_dir.join("file2.csv"))
    assert os.path.exists(temporary_output_dir.join("file3.csv"))
