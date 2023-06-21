import pytest
import os
import pandas as pd

from src.main import loadData, deleteOutputFiles, createOutputDir

OUTPUT_PATH = "tests/unit/data_validation/output/"
OUTPUT_CONFIG = {
    "customers": ["customer_id", "city", "country"],
    "products": ["product_id", "product_name"],
    "order_items": ["order_id", "customer_id", "product_id", "quantity", "price_gbp"],
}


def test_loadData_files_created():
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
    df = pd.DataFrame(sample_data)

    createOutputDir("tests/unit/data_validation/")
    deleteOutputFiles(OUTPUT_PATH)
    loadData(df, OUTPUT_PATH)

    # Assert that the output files are created in the temporary directory
    customers_file = os.path.join(OUTPUT_PATH, "customers.csv")
    order_items_file = os.path.join(OUTPUT_PATH, "order_items.csv")
    products_file = os.path.join(OUTPUT_PATH, "products.csv")

    assert os.path.exists(customers_file)
    assert os.path.exists(order_items_file)
    assert os.path.exists(products_file)


# Use @pytest.mark.dependency decorator to the test functions and specify the dependency
@pytest.mark.dependency(depends=["test_loadData_files_created"])
def test_checkColumns():
    # Read the output files
    customers_path = f"{OUTPUT_PATH}customers.csv"
    order_items_path = f"{OUTPUT_PATH}order_items.csv"
    products_path = f"{OUTPUT_PATH}products.csv"

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
        assert len(df) > 0  # Additional assertion to ensure data is not empty


@pytest.mark.dependency(depends=["test_loadData_files_created"])
def test_checkColumnsNoNullValues():
    # Read the output files
    customers_path = f"{OUTPUT_PATH}customers.csv"
    order_items_path = f"{OUTPUT_PATH}order_items.csv"
    products_path = f"{OUTPUT_PATH}products.csv"

    # Perform assertions for each file
    for path in [customers_path, order_items_path, products_path]:
        df = pd.read_csv(path)

        # Check if there are no null/None values in each column
        for column in df.columns:
            assert not df[column].isnull().any()


@pytest.mark.dependency(depends=["test_loadData_files_created"])
def test_checkQuantityGreaterThanZero():
    # Read the order_times file
    df = pd.read_csv(f"{OUTPUT_PATH}order_items.csv")
    assert (df["quantity"] > 0).all()


# TODO use temporary paths and clean up after tests
