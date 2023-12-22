"""
This is a boilerplate pipeline 'data_engineering'
generated using Kedro 0.18.14
"""

from kedro.pipeline import Pipeline, pipeline, node
from .nodes import scrub_data, prepare_data, creating_train_test_splits


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func=scrub_data,
            inputs=["hr_data_recieved", "params:drop_cols"],
            outputs="scrubbed_data",
            name="node_scrub_data"
        ),
        node(
            func=prepare_data,
            inputs=["scrubbed_data", "params:need_dummy_cols"],
            outputs= ["X_scaled", "Y"],
            name="node_prepare_data"
        ),
        node(
            func=creating_train_test_splits,
            inputs=["X_scaled", "Y", "params:test_size", "params:random_state"],
            outputs=["x_train", "x_test", "y_train", "y_test"],
            name="node_train_test_split"
        )
    ])
