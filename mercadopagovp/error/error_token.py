

class ErrorTokenValue(Exception):
    def __init__(self, token_value) -> None:
        super().__init__(f'error token value: {token_value}')