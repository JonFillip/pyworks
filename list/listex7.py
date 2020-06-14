def format_list(args, separator=', '):
    """Takes a list and prints a formatted string"""
    if args == '' or args == []:
        return 'No value entered'
    else:
        parser = separator.join(args[0:-1])
        return f"{parser} and {args[-1]}"

spam = []
print(format_list(spam))