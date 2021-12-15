print('\n      Crazy examples')
p = lambda: print('oho')
p()
pp = lambda: lambda: print('ohoho')
pp()()

q = lambda x: print('hey', x)
q(5)
qq = lambda x: lambda x: print('heyhey', x)
qq(5)
qq(5)(6)
qqq = lambda x: lambda y: print('heyheyhey', x, y)
qqq(5)
qqq(5)(6)

print('\n      Many calls')


def rec(p):
    if p is None:
        return 1
    else:
        return p + 1


print(rec(10))
print(rec(rec(10)))
print(rec(rec(rec(rec(rec(rec(None)))))))


class SelfIdent:
    def __init__(self):
        self.d = 0

    def self_ident(self):
        self.d += 1
        return self.self_ident


si = SelfIdent()
si.self_ident()()()()()()()()()()()()()()
print(si.d)
