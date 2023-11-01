# 모듈 사용
# import Day06_module

# Day06_module.price(3) # 3명이서 영화 보러 갔을 때 가격
# Day06_module.price_morning(4) # 4명이서 조조 할인 영화 보러 갔을 때
# Day06_module.price_soldier(5) # 5명의 군인이 영화 보러 갔을 때

# as를 통해서 별칭을 줄 수 있다.
# import Day06_module as mv
# mv.price(3)
# mv.price_morning(4)
# mv.price_soldier(5)

# from Day06_module import *
# price(3)
# price_morning(4)
# price_soldier(5)

# from Day06_module import price, price_morning
# price(3)
# price_morning(4)

from Day06_module import price_soldier as price
price(5) 