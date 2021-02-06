# def hanoi(n, from_pos, to_pos, aux_pos):
#     if n == 1:
#         print(from_pos,"->",to_pos)
#         return
#
#     hanoi(n-1, from_pos, aux_pos, to_pos)
#     print(from_pos, "->", to_pos)
#     hanoi(n-1, aux_pos, to_pos, from_pos)
#
#
# hanoi(4, 1, 3, 2)

# 6-1
# 1)
# import turtle as t
#
#
# def many_squares(n):
#     if n <= 2:
#         t.done()
#         return
#
#     t.forward(n)
#     t.right(90)
#     many_squares(n-2)
#
#
# t.speed(0)
# many_squares(40)
# t.hideturtle()
# t.done()

# 2)

# import turtle as t
#
#
# def many_triangles(n):
#     if n < 2:
#         return
#
#     many_triangles(n / 2)
#     t.seth(0)
#     t.forward(n)
#     many_triangles(n / 2)
#     t.seth(0)
#     t.forward(n)
#     t.seth(120)
#     t.forward(2 * n)
#     t.seth(240)
#     t.forward(n)
#     many_triangles(n / 2)
#     t.seth(240)
#     t.forward(n)
#
#
# t.speed(0)
# many_triangles(100)
# t.done()

# 3)
# import turtle as t
#
#
# def tree(n):
#     current_angle = t.heading()
#     t.forward(n)
#     if n > 5:
#         t.left(30)
#         tree(n * 0.7)
#         t.seth(current_angle-30)
#         tree(n * 0.7)
#         t.seth(current_angle)
#     t.back(n)
#
#
# t.speed(0)
# t.seth(90)
# tree(50)
# t.done()


# 4) 대충 이해는 했지만... 얘는 제대로 코딩하진 않(못)했습니다
# import turtle as t
# def snow_line(snow_len):
#     if snow_len <= 10:
#         t.forward(snow_len)
#         return
#     new_len = snow_len / 3
#     snow_line(new_len)
#     t.left(60)
#     snow_line(new_len)
#     t.right(120)
#     snow_line(new_len)
#     t.left(60)
#     snow_line(new_len)
#
#
# t.speed(0)
# snow_line(150)
# t.done()
