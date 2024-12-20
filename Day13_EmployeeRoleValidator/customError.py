class InvalidRoleError(TypeError):
    def __init__(self, message):
        super().__init__(f'InvalidRoleError: The provided object is not a valid Employee type. {message}')
