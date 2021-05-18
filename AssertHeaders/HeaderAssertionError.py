class HeaderAssertionError(Exception):
    def __init__(self, errors):
        self.errors = errors
        self.message = "The following header errors occurred:\n- " + "\n- ".join(map(lambda error: error.get("message"), errors))
        super().__init__(self.message)
