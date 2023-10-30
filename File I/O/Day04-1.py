# 파일 입출력
# 파이썬을 이용해서 파일을 열어서 내용을 넣고 가져올 수 있음
# open메서드를 통해서 파일에 접근 할 수 있다.
# 예시 : open(파일명, 모드방식, 인코딩방식)

# 쓰기 모드 'w' 사용해서 파일에 새로운 데이터 작성
# (만약 데이터가 있다면 기존 데이터가 사라지고 새로 입력한 데이터가 덮어씌워짐)
score_file = open("score.txt", "w", encoding="utf-8")
score_file.write("수학 : 0\n")
score_file.write("영어 : 50")
score_file.close()

# 추가 모드 'a'를 사용해서 기존 데이터에 추가로 새로운 데이터 작성(파일 끝에 내용을 추가)
score_file = open("score.txt" , "a", encoding="utf-8")
score_file.write("\n과학 : 80")
score_file.write("\n코딩 : 100")
score_file.close()

#읽기 모드 'r'를 사용해서 파일에 있는 데이터를 가져오기
# score_file = open("score.txt", "r", encoding="utf-8")
# print(score_file.read())
# score_file.close()


# score_file = open("score.txt", "r", encoding="utf-8")
# print(score_file.readline()) #readline메서드는 줄별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
# print(score_file.readline())
# print(score_file.readline())
# print(score_file.readline())
# score_file.close()

# # 만약 다른 사람의 파일을 readline으로 가져와야할 경우 는
# # 몇개의 줄이 있는지 모르기 때문에 while문을 이용해서 가져올 수 있음
# score_file = open("score.txt", "r", encoding="utf-8")
# while True :
#     line = score_file.readline()
#     if not line : break
#     print(line,end = "")
# score_file.close()

# # 리스트에 값을 전부 담아 처리가능
# score_file = open("score.txt", "r", encoding="utf-8")
# lines = score_file.readlines() # list 형태로 저장
# for line in lines :
#     print(line,end = "")
# score_file.close()    


# pickle
# 프로그램상에서 지금 사용하고 있는 데이터를 file로 저장해줌
import pickle
profile_file = open("profile.pickle", "wb")
profile = {"이름":"박명수", "나이":30, "취미":["축구", "골프", "코딩"]}
print(profile)
pickle.dump(profile,profile_file) # profile에 있는 정보를 profile_file.txt파일 에 저장
profile_file.close()

profile_file = open("profile.pickle", "rb")
profile = pickle.load(profile_file) #file에 있는 정보를 profile 에 불러오기
print(profile)
profile_file.close()

# with
# 리소스를 열고 사용한 후 자동으로 닫아주는 역할
import pickle

with open("profile.pickle", "rb") as profile_file : 
    print(pickle.load(profile_file))

with open("study.txt", "w", encoding="utf-8") as study_file :
    study_file.write("파이썬을 공부하는 중..")

with open("study.txt" , "r", encoding="utf-8") as study_file :
    print(study_file.read())

#실습
# #당신의 회사에서는 매주 1회 작성해야 하는 보고서가 있습니다.
# 보고서는 항상 아래와 같은 형태로 출력되어야 합니다.
# 
# - X 주차 주간보고 -
# 부서 :
# 이름 :
# 업무 요약 :
# 
# 1주차부터 50주차까지의 보고서 파일을 만드는 프로그램을 작성하시오.
# 
# 조건 : 파일명은 '1주차.txt', '2주차.txt', ... 와 같이 만듭니다.#    

for week in range(1 , 51) :
    with open(f"{week}주차.txt", "w", encoding="utf-8") as report :
        report.write(f"-{week}주차 주간보고-\n부서 : \n이름 : \n업무 요약 :")