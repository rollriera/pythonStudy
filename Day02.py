# 리스트 : 순서를 가지는 객체의 집합 [] Java의 배열
# Java에서는 배열과 컬랙션 객체인 ArrayList로써의 분배가 있지만 Python에서는 리스트라고 불리며 자바에서의 
# 배열과는 리스트의 index값이 동적으로 증가함

# 지하철 칸별로 10명, 20명, 30명 ~
subway = [10,20,30]
print(subway)

#Java에서는 Heap영역에 저장된 배열의 주소값이 출력되지만 Python은 배열의 데이터를 바로 출력
print(subway)

# 직접 index값으로도 접근이 가능함
print(subway[0])
print(subway[1])
print(subway[2])

# index 메서드를 이용해서 내가 원하는 값의 index값을 출력할 수도 있음
print(subway.index(20))

#append 메서드를 이용해서 데이터 추가도 가능함 append함수를 사용하면 항상 맨 뒤에 등록되게됨
subway.append(40)
print (subway)

#insert 메서드를 이용해서 추가하고 싶은 데이터의 위치도 지정할 수 있음
#예시 : subway.insert(index 위치값 , 추가하고싶은 데이터)
subway.insert(0 , 20)
print(subway)

#pop이라는 메서드를 통해서 데이터 한개씩만 제거 특정 index의 데이터도 제거 가능
print(subway.pop()) # 파라미터 값을 적지 않으면 뒤에서부터 하나만 제거 하고 제거한 데이터를 출력해줌
print(subway.pop(1)) # index값을 parameter로 넣고 삭제도 가능
print(subway)

#count 메서드를 통해서 동일한 데이터값이 몇개가 존재하는지 확인도 가능
print(subway.count(20))

#sort 메서드를 이용해서 오름차순 정렬도 가능
num_list = [5,2,4,3,1]
num_list.sort()
print(num_list)

#reverse 메서드를 이용해서 내림차순 정렬도 가능
num_list.reverse()
print(num_list)

# clear 메서드를 통해서 배열안에 있는 데이터도 삭제 가능
num_list.clear()
print(num_list)

#다양한 자료형 함께 사용 가능
num_list = [5,2,4,3,1]
mix_list = ["Python", 20, True]
print(mix_list)

#extend메서드를 이용해서 리스트 확장 가능
mix_list.extend(num_list)

#리스트를 확장했다고 접근 방법이 달라지진 않음
print(mix_list[0])
print(mix_list[1])
print(mix_list[2])
print(mix_list[3])
print(mix_list[4])
print(mix_list[5])
print(mix_list[6])
print(mix_list[7])

#딕셔너리 (key , value) Java에서의 Map 형식과 비슷함 int 나 String 타입으로도 키값을 선언 가능
cabinet = {1: "강아지", 3:"고양이"}

#대괄호 안에다가 키값을 입력하면 키값에 맵핑된 데이터가 출력됨
print(cabinet[3]) # Java에서의 Map.get(3);
print(cabinet[1])

print(cabinet.get(3)) #Java와 동일하게 get메서드가 있음

#주의점
#대괄호 안에다가 없는 키값을 입력했을 때는 Exception이 발생 되며 프로그램이 종료되지만
# print(cabinet[5])
#get메서드를 이용하면 None로 출력되면서 프로그램이 그대로 실행됨
print(cabinet.get(5))
print("test")

#만약 키값이 없는 경우에는 다른 방법으로도 처리가능
print(cabinet.get(5, "만약 해당 키값이 없으면 이 문장을 출력"))

# 해당 딕셔너리에 내가 찾고싶은 키가 있는지 확인도 가능
# 예시 : 키값 in 변수명 boolean타입으로 결과 반환
print(3 in cabinet) #True
print(5 in cabinet) #False

#딕셔너리에 새로운 데이터를 추가
# 예시 : 변수명[새로운 키값] = 맵핑할 데이터 기입
# 데이터를 추가하고 중복된 키값으로 만약 데이터를 넣는다고 한다면 
# 해당 키에 맵핑된 기존 데이터를  새로운 데이터로 덮어씌우게됨

cabinet[5] = "병아리"
print(5 in cabinet)
print(cabinet)
cabinet[5] = "부엉이"
print(cabinet)
print(5 in cabinet)
print(cabinet.get(5))