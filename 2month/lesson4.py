# class Test:
#
#     # Магические
#     def __init__(self, name):
#         self.name = name
#
#     def __str__(self):
#         return self.name
#
#
# # test_obj = Test("Ardager")
#
# # print(test_obj)
#
#
# class Vector:
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __add__(self, other):
#         return self.x + other.x
#
#     def __lt__(self, other):
#         print('<')
#         return self.y < other.y
#
#     def __gt__(self, other):
#         print(">")
#         return self.y > other.y
#
#     def __getitem__(self, item):
#         pass
#
# obj_1 = Vector(11, 12)
# obj_2 = Vector(22, 23)
#
#
# # list_test = [1,2,3,4,5,6,7,8,89,9]
# #
# # print(list_test[3])









class Video:
    def __init__(self, title, description, file):
        self.title = title
        self.description = description
        self.file = file
        self.view_count = 0



    def view_count_up(self, user):
        pass

    def __call__(self, *args, **kwargs):
        self.view_count += 1
        print("View count up + 1")



first_video = Video("Just", "My video", "linlk")


# print(first_video.view_count)
# first_video()
# first_video()
# first_video()
# first_video()
# first_video()
# first_video()
# first_video()
# first_video()
# first_video()
# print(first_video.view_count)










class Money:

    def __init__(self, sum, currency):
        self.sum = sum
        self.currency = currency


    def convert_money(self, first, second):
        pass
    def __add__(self, other):
        if self.currency == other.currency:
            return self.sum + other.sum
        return self.convert_money(self, other)


