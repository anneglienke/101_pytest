import pytest
import os
import pandas as pd
from pathlib import Path
import shutil

from src.main import loadData

OUTPUT_PATH = "tests/unit/data_validation/output/"
OUTPUT_CONFIG = {
    "customers": ["customer_id", "city", "country"],
    "products": ["product_id", "product_name"],
    "order_items": ["order_id", "customer_id", "product_id", "quantity", "price_gbp"],
}
sample_data = {
    "product_id": [1, 1, 3, 2],
    "product_name": ["Toaster", "Toaster", "Speaker", "TV"],
    "quantity": [2, 1, 1, 1],
    "price_gbp": [29.99, 29.99, 49.99, 549.99],
    "order_id": [1, 2, 3, 3],
    "customer_id": [5, 6, 10, 10],
    "city": ["London", "Manchester", "San Francisco", "San Francisco"],
    "country": ["UK", "UK", "USA", "USA"],
}


def createTempOutputDir():
    output_dir = Path(OUTPUT_PATH)

    if not os.path.exists(output_dir):
        output_dir.mkdir()

    return output_dir


def deleteTempOutputDir(output_dir):
    shutil.rmtree(output_dir)


def test_loadData_files_created():
    # Create df
    df = pd.DataFrame(sample_data)

    # Create temporary output directory
    createTempOutputDir()
    output_dir = createTempOutputDir()

    # Execute function being tested
    loadData(df, OUTPUT_PATH)

    # Assert that the output files are created in the temporary directory
    customers_path = output_dir / "customers.csv"
    order_items_path = output_dir / "order_items.csv"
    products_path = output_dir / "products.csv"

    assert customers_path.exists()
    assert order_items_path.exists()
    assert products_path.exists()
    return output_dir, customers_path, order_items_path, products_path


# Use @pytest.mark.dependency decorator to the test functions and specify the dependency
@pytest.mark.dependency(depends=["test_loadData_files_created"])
def test_checkColumns():
    # Read the output files
    (
        output_dir,
        customers_path,
        order_items_path,
        products_path,
    ) = test_loadData_files_created()

    # Define the expected columns for each output file
    expected_columns = {
        "customers": OUTPUT_CONFIG["customers"],
        "order_items": OUTPUT_CONFIG["order_items"],
        "products": OUTPUT_CONFIG["products"],
    }

    # Perform assertions for each file
    for key in expected_columns:
        file_path = {
            "customers": customers_path,
            "order_items": order_items_path,
            "products": products_path,
        }[key]

        df = pd.read_csv(file_path)
        actual_cols = list(df.columns)

        # Exclude "index" column from the left side of the assertion
        assert actual_cols[1:] == expected_columns[key][:]
        assert len(df) > 0  # Ensure data is not empty

    # Delete temporary output directory
    deleteTempOutputDir(output_dir)
    assert not output_dir.exists()
