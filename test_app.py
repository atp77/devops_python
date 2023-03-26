from app import fib

def test_fib():
    assert "3" in fib("2")
    assert "4" in fib("3")
    assert "5" in fib("5")
    assert "6" in fib("8")
    assert "7" in fib("13")
    assert "0" in fib("0")
    assert "1" in fib("1")
    assert "2" in fib("1")

    

