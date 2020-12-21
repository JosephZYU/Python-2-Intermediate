# # https://youtu.be/kr0mpwqttM0

# def square(num):
#     return num ** 2


# def cube(num):
#     return num ** 3


# def my_mapping(func, arg_list):
#     results = []
#     for i in arg_list:
#         results.append(func(i))
#     return results


# list_1 = list(range(10))


# print(my_mapping(square, list_1))
# print(my_mapping(cube, list_1))


# def logger(msg):

#     def log_message():
#         print(f"Log: {msg}")

#     return log_message


# print(logger('Good Morning from AWS')())

# "".format is great to repetitive variable printout E.g. 0102030123

def html_tag(tag):

    def wrap_text(msg):
        print("<{0}>{1}</{0}>".format(tag, msg))

    return wrap_text


print(html_tag('Joseph')('Yu'))
