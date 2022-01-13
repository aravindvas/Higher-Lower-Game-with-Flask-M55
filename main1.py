def log_decr(f):
    def wrp(*args, **kwargs):
        print(f"u called  {f.__name__}{args}")
        rslt = f(args[0], args[1], args[2])
        print(f"returned: {rslt}")
    return wrp

@log_decr
def a_f(a,b,c):
    return a*b*c

a_f(1,2,3)
