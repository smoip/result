class Result:
    @classmethod
    def succeed(cls, content = None):
        result = cls()
        result._succeed(content)
        return result

    @classmethod
    def fail(cls, error = None):
        result = cls()
        result._fail(error)
        return result

    def _succeed(self, content):
        self.success = True
        self.content = content
        self.validate()

    def _fail(self, error):
        self.success = False
        self.error = error
        self.validate()

    def validate(self):
        if self.success:
            # empty iterables are valid return values
            assert self.content or len(self.content) == 0
        else:
            assert self.error
        assert not (hasattr(self, "content") and hasattr(self, "error"))
        self.failure = not self.success
