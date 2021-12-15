# In function definition we use formal parameters.
# In function call we use actual parameters (arguments)


print('   Standard parameters - positional or keyword')


def standard(p1, p2, p3):
    print(p1, p2, p3)


standard(1, 2, 3)
standard(p3=3, p2=2, p1=1)

print('   Positional only')


def pos_only(p1, p2, /, p3):
    print(p1, p2, p3)


pos_only(1, 2, 3)
pos_only(1, 2, p3=3)

print('   kwd only')


def kwd_only(p1, *, p2, p3):
    print(p1, p2, p3)


kwd_only(1, p3=3, p2=2)

print('   Mixed: pos only,standard (pos or kwd),kwd only')


def mix(p1, /, p2, *, p3):
    print(p1, p2, p3)


mix(1, 2, p3=3)
mix(1, p2=2, p3=3)

print('   Default arguments')


def mix_with_defaults(p1, p2, /, p3, p4=100, *, p5=101, p6):
    print(p1, p2, p3, p4, p5, p6)


mix_with_defaults(1, 2, 3, 4, p5=5, p6=6)
mix_with_defaults(1, 2, 3, p5=5, p6=6)
mix_with_defaults(1, 2, 3, p6=6)

print('   Variable-length parameters (arbitrary parameters)')

print('   Arbitrary pos parameters')


def arbitrary_pos(*p1):
    print(p1)


arbitrary_pos(1, 2)
arbitrary_pos(1, 2, 3, 4, 5, 6, 7)

print('   Arbitrary kwd parameters')


def arbitrary_kwd(**p1):
    print(p1)


arbitrary_kwd(n1=1, n2=2)
arbitrary_kwd(n1=1, n7=7, n4=4, n3=3)

print('   The order of parameters')

print('   f(pos_only,...,/,pos_or_kwd,...,*,kwd_only)')


def all_par_kinds(p1, p2, /, p3, p4, *, p5, p6):
    print(p1, p2, p3, p4, p5, p6)


all_par_kinds(1, 2, 3, 4, p5=5, p6=6)


def all_par_kinds_and_arbitrary_pos(p1, p2, /, *p3, p4, p5):
    print(p1, p2, p3, p4, p5)


all_par_kinds_and_arbitrary_pos(1, 2, p4=4, p5=5)
all_par_kinds_and_arbitrary_pos(1, 2, 101, 102, p4=4, p5=5)

print('   In this example default value is not used:')


def all_par_kinds_and_arbitrary_pos_2(p1, p2=200, /, *p3, p4, p5):
    print(p1, p2, p3, p4, p5)


all_par_kinds_and_arbitrary_pos_2(1, 2, p4=4, p5=5)
all_par_kinds_and_arbitrary_pos_2(1, 2, 101, 102, p4=4, p5=5)
print('   In this example default value is used:')
all_par_kinds_and_arbitrary_pos_2(1, p4=4, p5=5)

print('   Arbitrary pos and kwd:')


def arbitrary_pos_and_kwd(*pos, **kwd):
    print(pos, kwd)


arbitrary_pos_and_kwd()
arbitrary_pos_and_kwd(1, p2=2)
arbitrary_pos_and_kwd(1, 2, 3, p6=6, p5=5, p4=4)

print('   Unpacking of arguments:')


def unpack_pos(p1, p2, p3):
    print(p1, p2, p3)


l = (1, 2, 3)
unpack_pos(*l)  # is the same as:
unpack_pos(1, 2, 3)  # or:
l1 = [1]
l2 = (2, 3)
unpack_pos(*l1, *l2)


def unpack_kwd(*, p4, p5, p6):
    print(p4, p5, p6)


d = {'p4': 4, 'p5': 5, 'p6': 6}
d1 = {'p4': 4}
d2 = {'p5': 5, 'p6': 6}

unpack_kwd(**d)  # is the same as:
unpack_kwd(p4=4, p5=5, p6=6)


def unpack_pos_and_kwd(p1, p2, p3, /, *, p4, p5, p6):
    print(p1, p2, p3, p4, p5, p6)


unpack_pos_and_kwd(*l, **d)  # is the same as:
unpack_pos_and_kwd(1, 2, 3, p4=4, p5=5, p6=6)  # or:
unpack_pos_and_kwd(*l1, *l2, **d1, **d2)  # or:
unpack_pos_and_kwd(*l1, *l2, **d2, **d1)  # but not:
unpack_pos_and_kwd(*l2, *l1, **d2, **d1)  # and not:
# unpack_pos_and_kwd(*l1, *d1, **l2, **d2)  # or:

print('   By the way: conditional assignment')

# Traditional:

a = 0
if a < 0:
    b = -1
else:
    b = 1
print(b)
# More convenient:
b = -1 if a < 0 else 1
print(b)
