# 7-1
# def search_for_indexes(target, element):
#     result = []
#     if not isinstance(target, list):
#         print("에러")
#         return
#
#
#     for i in range(0, len(target)):
#         if target[i] == element:
#             result.append(i)
#
#     return result
#
#
# example_list = [200, 99, 31, 99, 200]
# print(search_for_indexes(example_list, 200))

# 7-3
stu_no = [39, 14, 67, 105]
stu_name = ["Justin", "John", "Mike", "Summer"]


def zip_method(no):
    stu_dict = dict(zip(stu_no, stu_name))
    return "?" if stu_dict.get(no) is None else stu_dict[no]


def index_search_method(no):
    index = -1
    for i in range(0, len(stu_no)):
        if stu_no[i] == no:
            index = i
            break
    return "?" if index == -1 else stu_name[index]


print(zip_method(39))
print(zip_method(22))
print(index_search_method(39))
print(index_search_method(22))
