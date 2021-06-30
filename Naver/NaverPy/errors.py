class NaverPyException(Exception) :
    '''Basic Exception'''

class ArgumentError(NaverPyException) :
    '''Exception For Wrong Argument'''

class AuthenticationErro(NaverPyException) :
    '''Exception For Authentication Fail'''

class InternalServerError(NaverPyException) :
    '''Exception For Internal Server Error'''
    def __init__(self, *args: object) -> None:
        super().__init__('Server Error, Please report error to Developer Forum(https://developers.naver.com/forum)')