import cProfile

def test_loop():
    for _ in range(10**6):
        _ = sum(range(100))

cProfile.run('test_loop()')
