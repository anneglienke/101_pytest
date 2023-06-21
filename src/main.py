import json
import pandas as pd
import logging
import os
from cerberus import Validator

INPUT_PATH = "src/input/orders.jsonl"
OUTPUT_PATH = "src/output/"
OUTPUT_CONFIG = {
    "customers": ["customer_id", "city", "country"],
    "products": ["product_id", "product_name"],
    "order_items": ["order_id", "customer_id", "product_id", "quantity", "price_gbp"],
}
ORDERS_SCHEMA = {
    "order_id": {
        "type": "integer",
        "required": True,
        "nullable": False,
        "empty": False,
    },
    "customer_id": {
        "type": "integer",
        "required": True,
        "nullable": False,
        "empty": False,
    },
    "customer_city": {
        "type": "string",
        "required": True,
        "nullable": False,
        "empty": False,
    },
    "customer_country": {
        "type": "string",
        "required": True,
        "nullable": False,
        "empty": False,
    },
    "order_items": {
        "type": "list",
        "minlength": 1,
        "empty": False,
        "schema": {
            "type": "dict",
            "schema": {
                "product_id": {
                    "type": "integer",
                    "required": True,
                    "nullable": False,
                    "empty": False,
                },
                "product_name": {
                    "type": "string",
                    "required": True,
                    "nullable": False,
                    "empty": False,
                },
                "quantity": {
                    "type": "integer",
                    "required": True,
                    "nullable": False,
                    "empty": False,
                    "min": 1,
                },
                "price_gbp": {
                    "type": "number",
                    "required": True,
                    "nullable": False,
                    "empty": False,
                },
            },
        },
    },
}


# Set up logs
logging.basicConfig(format="[%(asctime)s] %(message)s", level=logging.INFO)


# Use a Cerberus to validate dicts according to schema
def validator(order, schema):
    v = Validator(schema)
    return v.validate(order), v.errors


def validateObjects(objects, schema):
    valid_objects = []
    for obj in objects:
        valid, errors = validator(obj, schema)
        if valid:
            valid_objects.append(obj)
        else:
            logging.info(f'Discarded invalid object(s): "{obj}", errors: {errors}')
    valid_rows = len(valid_objects)
    return valid_objects, valid_rows


# Open a .jsonl file and transform into a list of Python dicts
def extractData(dataset: str):
    # Open JSON file
    input_json = open(dataset, "r")
    extracted_objects = []
    # Iterate through each JSON object, convert JSON string into Python dict
    for obj in input_json:
        py_dict = json.loads(obj)
        extracted_objects.append(py_dict)
    logging.info(f"Loaded {len(extracted_objects)} rows.")
    return extracted_objects


# Transform order list by initializing a DataFrame with flattened nested values and renamed columns
def transformOrdersList(valid_orders: list, valid_rows: int):
    # Flatten order_items
    flat_df = pd.json_normalize(
        valid_orders,
        meta=["order_id", "customer_id", "customer_city", "customer_country"],
        record_path="order_items",
    )
    # Rename columns
    renamed_df = flat_df.rename(
        columns={"customer_city": "city", "customer_country": "country"}
    )
    logging.info(f"Created a dataframe with {valid_rows} valid rows.")
    return renamed_df


# Delete existing files on ./output/ directory
def deleteOutputFiles(output_path: str):
    # Get a list of all the files in the directory
    files = os.listdir(output_path)
    logging.info(f"Found the following file(s) in the output directory: {files}")
    for file in files:
        # Create the full path to the file
        file_path = os.path.join(output_path, file)
        # Delete the file
        os.remove(file_path)
    logging.info("Deleted all the files in the output directory")


def createOutputDir(dir):
    # Get the current working directory
    current_dir = os.getcwd()

    # Create the path for the "tests" folder
    tests_dir = os.path.join(current_dir, dir)

    # Create the path for the "output" folder inside the "tests" folder
    output_dir = os.path.join(tests_dir, "output")

    # Create the "output" folder if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)


# Assemble output data as configured in OUTPUT_CONFIG, remove duplicates and create CSV files
def loadData(df: pd.DataFrame, output_path):
    for file_name, cols in OUTPUT_CONFIG.items():
        # Drop duplicates
        deduplicated_df = df.drop_duplicates(
            subset=cols, keep="first", ignore_index=True
        )
        # Create CSV file
        deduplicated_df.to_csv(
            f"{output_path}{file_name}.csv",
            sep=",",
            columns=cols,
            header=True,
            index_label="index",
        )
        print("loaded to csv")
        logging.info(f'Created CSV file "{file_name}.csv"')


def execute():
    extracted_objects = extractData(INPUT_PATH)
    valid_orders, valid_rows = validateObjects(extracted_objects, ORDERS_SCHEMA)
    df = transformOrdersList(valid_orders, valid_rows)
    createOutputDir("src")
    deleteOutputFiles(OUTPUT_PATH)
    loadData(df, OUTPUT_PATH)


execute()
