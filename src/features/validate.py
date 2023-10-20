import great_expectations as gx
import numpy as np
import pandas as pd

# Get the data context
context = gx.get_context()


# Create an Expectation Suite
context.add_or_update_expectation_suite("food_training_suite")


# Add a Pandas datasource to our context
datasource = context.sources.add_or_update_pandas(name="food_dataset")

PROCESSED_DATA_DIR = "/Users/violeta/Desktop/gced/Q7/TAED2/project1/taed2-Food_Classification/data/processed/"

x_train = pd.read_csv(PROCESSED_DATA_DIR + "x_data_information.csv")
y_train = pd.read_csv(PROCESSED_DATA_DIR + "y_data_information.csv")

train = pd.concat([x_train, y_train], axis=1)

data_asset = datasource.add_dataframe_asset(name="training", dataframe=train)


# Create a validator and configure the expectations
batch_request = data_asset.build_batch_request()
validator = context.get_validator(
    batch_request=batch_request,
    expectation_suite_name="food_training_suite",
    datasource_name="food_dataset",
    data_asset_name="training",
)


validator.expect_table_columns_to_match_ordered_list(
    column_list=[
        'size_dim1',
        'size_dim2',
        'size_dim3',
        'min_colour_range',
        'max_colour_range',
        'type_torch.float32',
        'label_id'
    ]
)

validator.expect_column_values_to_not_be_null('size_dim1')
validator.expect_column_values_to_not_be_null('size_dim2')
validator.expect_column_values_to_not_be_null('size_dim3')
validator.expect_column_values_to_not_be_null('min_colour_range')
validator.expect_column_values_to_not_be_null('max_colour_range')
validator.expect_column_values_to_not_be_null('type_torch.float32')
validator.expect_column_values_to_not_be_null('label_id')

validator.expect_column_values_to_be_between("min_colour_range", min_value=0)
validator.expect_column_values_to_be_between("max_colour_range", max_value=1)

validator.expect_column_values_to_be_in_set("size_dim1", [3.0])
validator.expect_column_values_to_be_in_set("size_dim2", [224.0])
validator.expect_column_values_to_be_in_set("size_dim3", [224.0])

validator.expect_column_values_to_be_of_type("label_id", "int64")

validator.expect_column_values_to_be_in_set("type_torch.float32", [1])

validator.expect_column_values_to_be_between("label_id", min_value=0)
validator.expect_column_values_to_be_between("label_id", max_value=29)


validator.save_expectation_suite(discard_failed_expectations=False)

# Create a checkpoint and run the validation
checkpoint = context.add_or_update_checkpoint(
    name="my_checkpoint",
    validator=validator,
)

checkpoint_result = checkpoint.run()
context.view_validation_result(checkpoint_result)
