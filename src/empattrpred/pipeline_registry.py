"""Project pipelines."""
from __future__ import annotations

from kedro.framework.project import find_pipelines
from kedro.pipeline import Pipeline
from empattrpred.pipelines import (
    data_engineering as de,
    data_science as ds,
    model_evaluation as me
)


def register_pipelines() -> dict[str, Pipeline]:
    """Register the project's pipelines.

    Returns:
        A mapping from pipeline names to ``Pipeline`` objects.
    """
    # pipelines = find_pipelines()
    # pipelines["__default__"] = sum(pipelines.values())
    # return pipelines
    data_engineering_pipeline = de.create_pipeline()
    data_science_pipeline = ds.create_pipeline()
    model_evaluation_pipeline = me.create_pipeline()
    return {
        "de": data_engineering_pipeline,
        "ds": data_science_pipeline,
        "me": model_evaluation_pipeline,
        "__default__": data_engineering_pipeline + data_science_pipeline + model_evaluation_pipeline
    }
