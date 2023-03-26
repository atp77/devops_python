from app import fib

def test_fib():
    assert 2 in fib(3)
    assert "3" in fib(4)
    assert "5" in fib(5)
    assert "8" in fib(6)
    assert "13" in fib(7)
    assert "0" in fib(0)
    assert "1" in fib(1)
    assert "1" in fib(2)

    

