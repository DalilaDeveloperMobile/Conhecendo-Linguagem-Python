# Modo Interativo
# Nesse modo posso interagir com meu código
# de forma automatica sem precisar executar
# varias vezes o código facilitando a codificação.

# Iniciar
# Digitar no Teminal a Palavra python.

# PS C:\Users\CLIENTE> python
# Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
# Type "help", "copyright", "credits" or "license" for more information.
# >>> 

# Não preciso ficar execultando o print

# PS C:\Users\CLIENTE> python
# Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
# Type "help", "copyright", "credits" or "license" for more information.
# >>> 10 + 10
# 20
# >>>

# Resultado
# 10 + 10 = 20 

# Para Sair
# exit()

# PS C:\Users\CLIENTE> python
# Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
# Type "help", "copyright", "credits" or "license" for more information.
# >>> 10 + 10
# 20
# >>> exit()
# PS C:\Users\CLIENTE> 

# Execultar Arquivo Expecifico:
# python -i primeiro_programa.py
# Resultado:
# Oi, seja bem vindo ao curso de Python!


# Função dir()

# dir() Retorna o escopo local.

# PS C:\Users\CLIENTE> python                        
# Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
# Type "help", "copyright", "credits" or "license" for more information.
# >>> dir()
# ['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__']
# >>> 

# dir(100) Retorna todos os
# metodos que o objeto cem tem.

# PS C:\Users\CLIENTE> python
# Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
# Type "help", "copyright", "credits" or "license" for more information.
# >>> dir(100)
# ['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'as_integer_ratio', 'bit_count', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'is_integer', 'numerator', 'real', 'to_bytes']
# >>>

# Função help()

# Iniciar help()

# PS C:\Users\CLIENTE> python
# Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
# Type "help", "copyright", "credits" or "license" for more information.
# >>> help()

# Welcome to Python 3.12's help utility! If this is your first time using
# Python, you should definitely check out the tutorial at
# https://docs.python.org/3.12/tutorial/.

# Enter the name of any module, keyword, or topic to get help on writing
# Python programs and using Python modules.  To get a list of available
# modules, keywords, symbols, or topics, enter "modules", "keywords",
# "symbols", or "topics".

# Each module also comes with a one-line summary of what it does; to list
# the modules whose name or summary contain a given string such as "spam",
# enter "modules spam".

# To quit this help utility and return to the interpreter,
# enter "q" or "quit".

# help>

# help> int 
# exibi todos os metodos da classe.
# Help on class int in module builtins:

# class int(object)
#  |  int([x]) -> integer
#  |  int(x, base=10) -> integer
#  |
#  |  Convert a number or string to an integer, or return 0 if no arguments
#  |  are given.  If x is a number, return x.__int__().  For floating point
#  |  numbers, this truncates towards zero.
#  |
#  |  If x is not a number or if base is given, then x must be a string,
#  |  bytes, or bytearray instance representing an integer literal in the
#  |  given base.  The literal can be preceded by '+' or '-' and be surrounded
#  |  by whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.
#  |  Base 0 means to interpret the base from the string as an integer literal.
#  |  >>> int('0b100', base=0)
#  |  4
#  |
#  |  Built-in subclasses:
#  |      bool
#  |
#  |  Methods defined here:
#  |
#  |  __abs__(self, /)
#  |      abs(self)
#  |
#  |  __add__(self, value, /)
#  |      Return self+value.
#  |
#  |  __and__(self, value, /)
#  |      Return self&value.
#  |
#  |  __bool__(self, /)
#  |      True if self else False
#  |
#  |  __ceil__(...)
#  |      Ceiling of an Integral returns itself.
#  |
#  |  __divmod__(self, value, /)
# -- Mais  -- 

# >>> help(100)
# Exibi a classe e os metodos da classe do objeto.

# Help on int object:

# class int(object)
#  |  int([x]) -> integer
#  |  int(x, base=10) -> integer
#  |
#  |  Convert a number or string to an integer, or return 0 if no arguments
#  |  are given.  If x is a number, return x.__int__().  For floating point
#  |  numbers, this truncates towards zero.
#  |
#  |  If x is not a number or if base is given, then x must be a string,
#  |  bytes, or bytearray instance representing an integer literal in the
#  |  given base.  The literal can be preceded by '+' or '-' and be surrounded
#  |  by whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.
#  |  Base 0 means to interpret the base from the string as an integer literal.
#  |  >>> int('0b100', base=0)
#  |  4
#  |
#  |  Built-in subclasses:
#  |      bool
#  |
# -- Mais  --
