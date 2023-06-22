## Tests/checks/monitors covered by this project (in progress...)

</br>

### 1 Unit Test
Verifies the functionality of individual components or units within the data pipeline. It focuses on testing specific functions, transformations, or modules in isolation. </br>
Example: 
- [test_deleteOutputFile](unit/test_deleteOutputFile.py)
- [test_transformOrdersList](unit/test_transformOrdersList.py)

</br>

#### 1.1 Error Handling Test
Verifies how the data pipeline handles errors, exceptions, or unexpected scenarios. It checks if appropriate error messages are generated, and error recovery mechanisms are in place.

</br>

#### 1.2 Data Validation Test
Ensures that the data pipeline adheres to predefined contracts: rules, constraints, or expectations. It validates data against defined schemas, formats, or business rules to maintain data integrity. </br>
Example: 
- [test_loadData](unit/test_loadData.py) ensures the function `loadData()` creates the output files and validates their schema.
- [test_validator](unit/test_validator.py) unit tests the function `validator()`, checking if it deals with valid and invalid inputs correctly. In [main.py](src/main.py), the same function is used to monitor inputs in run time.

</br>

### 2 Integration Test
Ensures that different components of the data pipeline work together correctly. It validates the interaction and compatibility between various stages or modules of the pipeline.

</br>

## Not covered

</br>

### Data Quality Monitoring 
Verifies the quality, accuracy, and completeness of the data flowing through the pipeline. It checks for anomalies, inconsistencies, missing values, or data integrity issued in run time.

