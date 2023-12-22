"""
This is a boilerplate pipeline 'data_science'
generated using Kedro 0.18.14
"""

from kedro.pipeline import Pipeline, pipeline, node
from .nodes import train_model, predict


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func=train_model,
             inputs= ["x_train", "y_train"],
             outputs= "ml_model",
             name="node_train_model"
        ),
        node(
            func=predict,
            inputs= ["ml_model", "x_test"],
            outputs= "predictions",
            name= "node_predictions"
        )
    ])
