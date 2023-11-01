# import 할때
# 패키지.파일 부분에 파일만 들어올 수 있다.
# 클래스를 호출하고 싶다면 from ~ import문 사용
import travel.thailand
trip_to = travel.thailand.ThailandPackage()
trip_to.detail()

from travel.thailand import ThailandPackage 