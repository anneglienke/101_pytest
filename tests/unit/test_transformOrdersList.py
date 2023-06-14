import pandas as pd

from src.main import transformOrdersList


def test_transformOrdersList():
    # Example input
    valid_orders = [
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
    valid_rows = len(valid_orders)

    # Call the function under test
    result_df = transformOrdersList(valid_orders, valid_rows)

    # Perform assertions on the transformed DataFrame
    assert isinstance(result_df, pd.DataFrame)
    assert len(result_df) == valid_rows

    # Add more specific assertions on the DataFrame as needed
    assert "order_id" in result_df.columns
    assert "customer_id" in result_df.columns
    assert "city" in result_df.columns
    assert "country" in result_df.columns
    assert "product_id" in result_df.columns
    assert "product_name" in result_df.columns
    assert "quantity" in result_df.columns
    assert "price_gbp" in result_df.columns
