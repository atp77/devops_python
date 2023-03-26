from app import fib

def test_fib():
    assert 2 == fib(3)
    assert 3 == fib(4)
    assert 5 == fib(5)
    assert 8 == fib(6)
    assert 13 == fib(7)
    assert 0 == fib(0)
    assert 1 == fib(1)
    assert 1 == fib(2)

    

