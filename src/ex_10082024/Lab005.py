import keyword
print(keyword.kwlist)
#['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']


# checking type of variables
print(type(12),type('hello'),type(True))
complex_number = 2+3j

print(complex_number.real)
print(complex_number.imag)

lst=[10,20,30]
print(sum(lst)) # does not works correctly when variables passed separately