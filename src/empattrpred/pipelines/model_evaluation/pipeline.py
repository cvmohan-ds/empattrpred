"""
This is a boilerplate pipeline 'model_evaluation'
generated using Kedro 0.18.14
"""

from kedro.pipeline import Pipeline, pipeline, node
from .nodes import train_evaluation, test_evaluation


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func=train_evaluation,
            inputs=["ml_model", "x_train", "y_train"],
            outputs=["train_classification_report", "train_evaluation"],
            name="node_train_evaluation"
        ),
        node(
            func=test_evaluation,
            inputs=["predictions", "y_test"],
            outputs=["test_classifcation_report", "test_evaluation"]
        )
    ])
