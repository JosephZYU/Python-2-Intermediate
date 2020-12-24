# https://youtu.be/FsAPt_9Bf3U

# 🤏⏭ https://youtu.be/FsAPt_9Bf3U?t=976


# 😎 Add our pre-built functions "inside" our wrapper


"""def decorator_func(original_func):
    def wrapper_func():
        print(f'Our wrapper executed before {original_func.__name__}')
        return original_func

    return wrapper_func()"""


def decorator_func(original_func):
    def wrapper_func(*args, **kwargs):
        print(f'Our wrapper executed before {original_func.__name__}')
        return original_func(*args, **kwargs)

    return wrapper_func


class decorator_class(object):
    def __init__(self, original_func):
        self.original_func = original_func

    def __call__(self, *args, **kwargs):
        print(f'Our Call method executed before {self.original_func.__name__}')
        return self.original_func(*args, **kwargs)


@decorator_func
def display():
    print('Display function ran by Joseph')


@decorator_func
def display_info(name, age):
    print(f'Display information ran with arguments ({name}, {age})')


display_info('Joseph', 33)
