class HistogramStrategy:
    def read(self, file_path):
        raise NotImplementedError("Must implement read")

    def write(self, file_path, histogram):
        raise NotImplementedError("Must implement write")


class HistogramContext:
    def __init__(self, strategy: HistogramStrategy):
        self.strategy = strategy

    def execute_read(self, file_path):
        return self.strategy.read(file_path)

    def execute_write(self, file_path, histogram):
        self.strategy.write(file_path, histogram)
