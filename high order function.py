# def loud(text):
#     return text.upper()
#
#
# def silence(text):
#     return text.lower()
#
# def speak(func):
#     text = func("Hi Wassup")
#     print(text)
#
# speak(silence)


def divisor(x):
    def dividend(y):
        return y/x
    return dividend

divide = divisor(7)

print(divide(21))


