def raises_value_error():
    raise ValueError


try:
    raises_value_error()
except ValueError:
    print("You raised a ValueError!")