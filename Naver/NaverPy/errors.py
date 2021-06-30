class NaverPyException(Exception) :
    '''Basic Exception'''

class ArgumentError(NaverPyException) :
    '''Exception For Wrong Argument'''

class InternalServerError(NaverPyException) :
    '''Exception For Internal Server Error'''