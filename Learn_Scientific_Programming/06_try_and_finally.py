# using try and finally
def f():
    try:
        1/0
    finally:
        return 42


print(f())
