#튜플 자료형

a = [1,2,3] #리스트

# t1 = ()
# print(type(t1))
# t2 = (1,)
# print(t2[0])
# t3 = (1, 2, 3)
# t4 = 1, 2, 3 => 튜플임
# print(type(t4)) 
# t5 = ('a', 'b', ('ab', 'cd'))
# t1 = (1, 2, 'a', 'b')
# del t1[0] 튜플은 변경이 불가능 하다.
# t1 = (1, 2, 'a', 'b')
# print(t1[0])
# print(t1[1])
# print(t1[2])
# print(t1[3])
# 튜플은 인덱싱이 가능하다.
# print(t1[1:])
# print(t1)
#튜플은 슬라이싱도 가능하다. 슬라이싱은 아무런 변형을 가하지 않고 보여주는 것 뿐이다.
#리스트는 변경 삭제가 가능하고 튜플은 변경이나 삭제가 불가능하다.

#튜플 더하기
# t1 = (1, 2, 'a', 'b')
# t2 = (3, 4)
# t3 = t1 + t2
# print(t3)
#더하기도 가능하다. t1이나 t2값을 변경하는게 아닌 더하기를 통해서 t3라는 새로운 튜플을 만드는 것이다.

#튜플 곱하기
# t2 = (3, 4)
# t3 = t2 * 3
# print(t3)

#튜플 길이 구하기
# t1 = (1, 2, 'a', 'b')
# print(len(t1))
