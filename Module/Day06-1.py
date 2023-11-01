# 모듈 사용
# import my_module

# my_module.price(3) # 3명이서 영화 보러 갔을 때 가격
# my_module.price_morning(4) # 4명이서 조조 할인 영화 보러 갔을 때
# my_module.price_soldier(5) # 5명의 군인이 영화 보러 갔을 때

# as를 통해서 별칭을 줄 수 있다.
import my_module as mv
mv.price_morning(4)
mv.price(3)
mv.price_soldier(5)

from my_module import *
price(3)
price_morning(4)
price_soldier(5)

from my_module import price, price_morning
price(3)
price_morning(4)

from pythonStudy.Module.my_module import price_soldier as price
price(5) 