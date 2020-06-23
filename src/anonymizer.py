from functools import partial
from functions import all_functions


class Anonymizer(object):
    def __init__(self, config: dict):
        self.processors = {}
        for processor_key in config:
            if processor_key in all_functions:
                processor_function = all_functions[processor_key]
                self.processors[processor_key] = partial(processor_function, config[processor_key])
            else:
                raise "Invalid anonymization method {} in configuration. Available are: {}".format(
                    processor_key, all_functions.keys())

    def process(self, data: [dict]):
        for process in self.processors.values():
            data = process(data)
        return data
