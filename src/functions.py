from collections import Iterable
import statistics
from functools import partial
from typing import Callable


def drop(config, data: [dict]):
    keys_to_delete = config.get("keys")
    for item in data:
        for key in keys_to_delete:
            item[key] = _new_value_from_type(item[key])
    return data


def _new_value_from_type(value):
    if isinstance(value, str):
        return ""
    if isinstance(value, Iterable):
        return []
    if isinstance(value, int):
        return 0
    # ...


def _replace_with_aggregate(aggregator: Callable, config, data: [dict]):
    keys_to_avg = config.get("keys")
    for key in keys_to_avg:
        avg = aggregator([item[key] for item in data])
        for item in data:
            item[key] = avg
    return data


mean = partial(_replace_with_aggregate, statistics.mean)
median = partial(_replace_with_aggregate, statistics.median)


def _get_function_name(fun):
    try:
        return fun.__name__
    except AttributeError:
        return fun.args[0].__name__


all_functions = {_get_function_name(f): f for f in [drop, mean, median]}
