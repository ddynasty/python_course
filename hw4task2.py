def mem_wrap(*args, **kwargs):

    def hashable_args(arguments):
        ishashble = True
        for args in arguments:
            if not isinstance(args, Hashable):
                ishashble = False
                break
        return ishashble
        if kwargs and not args:
            nargument = tuple([value for key, value in (sorted(kwargs.items()))])
            return ()
    return mem_wrap()

