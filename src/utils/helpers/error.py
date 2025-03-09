class InvalidDataSourceError(Exception):
    def __init__(self, data_source):
        super().__init__(f"Invalid data source: {data_source}")
        self.data_source = data_source