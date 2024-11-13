# FACTORIAL CALCULATION WITH A RECURSIVE FUNCTION

# WHAT IS TAIL-RECURSION?
# A unique type of recursion where the last procedure of a function is a recursive call.
# The recursion may be automated away by performing the request in the current stack frame and
# returning the output instead of generating a new stack frame.
# The tail-recursion may be optimized by the compiler which makes it better than non-tail recursive functions.



# non-tail-recursive function
# there's additional work to be done after the recursive call returns
def r_factor_nt(n):

    if n == 0:
        return 1

    return n * r_factor_nt(n-1)


print(r_factor_nt(6))



# tail-recursive function
# the recursive call is the last operation performed before returning
def r_factor_t(n, a = 1):

    if n == 0:
        return a

    return r_factor_t(n-1, n * a)


print(r_factor_t(6))