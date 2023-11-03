# def repeat_string(string, times):
#     return string * times
#
# some_text = input()
# n = int(input())
#
# print(repeat_string(some_text,n))

repeat_string = lambda string, times: string * times
some_text = input()
times = int(input())
print(repeat_string(some_text, times))