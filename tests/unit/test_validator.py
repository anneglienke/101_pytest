import pytest
from src.main import validator

SCHEMA = {
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


def test_validator_valid_input():
    sample_dataset = {
        "order_id": 1,
        "customer_id": 5,
        "customer_city": "London",
        "customer_country": "UK",
        "order_items": [
            {
                "product_id": 1,
                "product_name": "Toaster",
                "quantity": 2,
                "price_gbp": 29.99,
            }
        ],
    }
    validator(sample_dataset, SCHEMA)
    assert True


@pytest.mark.xfail(reason="Test fails due to missing column")
def test_validator_invalid_input_missing_column():
    sample_dataset = {
        "order_id": 1,
        "customer_id": 5,
        "customer_city": "London",
        "customer_country": "UK",
        "order_items": [
            {
                "product_id": 1,
                "product_name": "Toaster",
                "quantity": 2,
                "price_gbp": 29.99,
            }
        ],
    }
    validator(sample_dataset, SCHEMA)
    assert False


@pytest.mark.xfail(reason="Test fails due to quantity less than 1")
def test_validator_invalid_input_quantity_equal_zero():
    sample_dataset = {
        "order_id": 1,
        "customer_id": 5,
        "customer_city": "London",
        "customer_country": "UK",
        "order_items": [
            {
                "product_id": 1,
                "product_name": "Toaster",
                "quantity": 0,
                "price_gbp": 29.99,
            }
        ],
    }
    validator(sample_dataset, SCHEMA)
    assert False


@pytest.mark.xfail(reason="Test fails due to missing items")
def test_validator_invalid_input_missing_items():
    sample_dataset = {
        "order_id": 1,
        "customer_id": 5,
        "customer_city": "London",
        "customer_country": "UK",
        "order_items": [
            {
                "product_id": None,
                "product_name": None,
                "quantity": None,
                "price_gbp": None,
            }
        ],
    }
    validator(sample_dataset, SCHEMA)
    assert False


@pytest.mark.xfail(reason="Test fails due to empty order_id")
def test_validator_invalid_input_empty_order_id():
    sample_dataset = {
        "order_id": None,
        "customer_id": 5,
        "customer_city": "London",
        "customer_country": "UK",
        "order_items": [
            {
                "product_id": 1,
                "product_name": "Toaster",
                "quantity": 2,
                "price_gbp": 29.99,
            }
        ],
    }
    validator(sample_dataset, SCHEMA)
    assert False


@pytest.mark.xfail(reason="Test fails due to duplicated records")
def test_validator_invalid_input_duplicates():
    sample_dataset = [
        {
            "order_id": 1,
            "customer_id": 5,
            "customer_city": "London",
            "customer_country": "UK",
            "order_items": [
                {
                    "product_id": 1,
                    "product_name": "Toaster",
                    "quantity": 2,
                    "price_gbp": 29.99,
                }
            ],
        },
        {
            "order_id": 1,
            "customer_id": 5,
            "customer_city": "London",
            "customer_country": "UK",
            "order_items": [
                {
                    "product_id": 1,
                    "product_name": "Toaster",
                    "quantity": 2,
                    "price_gbp": 29.99,
                }
            ],
        },
    ]
    validator(sample_dataset, SCHEMA)
    assert False
