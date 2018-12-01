def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

def car(pair):
    getval = lambda a, b: a
    return pair(getval)

def cdr(pair):
    getval = lambda a, b: b
    return pair(getval)

def test_solution():
    cases = [
        ((3,4),3,4),
        ((4,3),4,3)
    ]

    for case in cases:
        a = case[0][0]
        b = case[0][1]
        gt_car = case[1]
        gt_cdr = case[2]
        assert car(cons(a,b)) == gt_car
        assert cdr(cons(a, b)) == gt_cdr
