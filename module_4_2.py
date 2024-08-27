def test_function():
    def inner_function():
        x = 'Я в области видимости функции test_function'
        return x
    return inner_function()


print(test_function())
print(inner_function())
