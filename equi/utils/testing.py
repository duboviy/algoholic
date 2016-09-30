""" Helper utility module used for testing. """


class TestData(object):

    def __init__(self, input_array, expected_result, expected_kstones=None):
        self.input_data = input_array
        self.expected_result = expected_result
        self.actual_result = None
        self.solution = None
        self.expected_kstones = expected_kstones    # PERFORMANCE UPPER LIMIT of algorithm
        self.actual_kstones = None
