import time
import random

print("""
  ___          _                    _   _____                         _               
 / _ \        (_)                  | | /  __ \                       (_)              
/ /_\ \ _ __   _  _ __ ___    __ _ | | | /  \/ _ __   ___   ___  ___  _  _ __    __ _ 
|  _  || '_ \ | || '_ ` _ \  / _` || | | |    | '__| / _ \ / __|/ __|| || '_ \  / _` |
| | | || | | || || | | | | || (_| || | | \__/\| |   | (_) |\__ \\__ \| || | | || (_| |
\_| |_/|_| |_||_||_| |_| |_| \__,_||_|  \____/|_|    \___/ |___/|___/|_||_| |_| \__, |
                                                                                 __/ |
                                                                                |___/ 
""")
print("~ 모여봐요 멋사의 숲 ~\n")

name = input("당신의 이름은? ") # 이곳을 채우세요
island = input("섬 이름은? (ㅇㅇ섬으로 입력됩니다) ") # 이곳을 채우세요

print(name + "님 반가워요! " + island + "섬에 오신것을 환영합니다-!")
time.sleep(1)

animal = {'릴리안': 0, '탁호': 0, '미첼': 0, '리처드': 0}
animal_key = list(animal.keys())
my_bell = 3000
my_pocket = []
store = {'가습기': 1400, '강아지 인형': 2400, '강의실 책상': 2500, '몬스테라': 1700}
store_key = ["가습기", "강아지 인형", "강의실 책상", "몬스테라"]

action_boolean = 1
store_buy = 0

# 4가지 반복하기
while action_boolean:
    print("\n어떤 것을 해볼까요?")
    answer_action = input("0. 종료 1. 상점가기 2. 주민 찾아가기 3. 나무 흔들기 4. 정보 확인하기 ")
    
    # 0. 게임 종료
    if answer_action == "0":
        action_boolean = 0

    # 1. 상점가기를 선택한경우
    elif answer_action == "1":
      print("상점에 온걸 환영해구리")
      time.sleep(0.5)
      print("현재 상점에는 이런 물건들이 있어구리\n")
      time.sleep(0.5)
      store_list = list(store.items())
      num = 1
      for i in store:
        print(num, ". ", i, ": ", store[i],  "벨")
        num += 1
        time.sleep(0.5)
        
      store_buy = input("\n어떤 물건을 구입하겠어구리? (숫자를 입력)")

      if store_list[int(store_buy) - 1][1] > my_bell:
        print("벨이 모자라 구입할 수 없습니다!")
      else :
        print(store_key[0], "을(를) 구입하셨습니다!")
        time.sleep(0.5)
        my_bell -= store_list[int(store_buy) - 1][1]
        print("남은 벨: ", str(my_bell))
        my_pocket.append(store_key[0])
        del store[store_list[int(store_buy) - 1][0]]
      time.sleep(0.5)
      
    # # 2. 주민 찾아가기를 선택한 경우
    elif answer_action == "2":
      print("\n우리 마을에 있는 주민이야")
      time.sleep(0.5)
      num = 1
      for i in animal:
        print(num, ". ", i)
        num += 1
        time.sleep(0.3)
      
      animal_list = list(animal.items())
      friend = input("\n어떤 주민을 찾아갈까?")
      print("\n", animal_list[int(friend) - 1][0], "에게 무엇을 할까?")
      answer_animal_action = input("1. 말걸기 2. 선물하기 3. 때리기")

      # 2-1. 말걸기를 선택한경우
      if answer_animal_action == "1":
        print("")
        # 릴리안에게 말걸기
        if(friend == "1") :
          print("어머 ", name, "왔구나~ 반가워!")
          time.sleep(0.3)
          print("어제는 어찌나 벚꽃이 이쁘던지 기분이 참 좋더라니까")
          time.sleep(0.3)
          print(name, "이도 놀러다녀오는건 어때? 그렇지뭐")

        # 탁호에게 말걸기
        if(friend == "2") :
          print("안녀엉~ ", name, "아~ 반가워어~")
          time.sleep(0.3)
          print("오늘 저녁은 뭘 먹을지 너무 고민이 돼~ 약히")

        # 미첼에게 말걸기
        if (friend == "3"):
          print(name, "아~! 반가워! 오늘 날씨 되게 좋지않아?")
          time.sleep(0.3)
          print("마구마구 산책을 하고싶어져 동글")

        # 리처드에게 말걸기
        if (friend == "4"):
          print(name, "야아~")
          time.sleep(0.3)
          print("나무를 흔들었더니 100벨이 나왔어어~")
          time.sleep(0.3)
          print(name, "도 한 번 흔들어봐아~ 그래유")

        animal[animal_key[int(friend) - 1]] += 1
        print(animal_key[int(friend) - 1], " 친밀도 +1")
        time.sleep(0.5)

      # 2-2. 선물하기를 선택한 경우
      elif answer_animal_action == "2":
        print("\n내 주머니엔 이런게 있어")
        num = 1
        for i in my_pocket:
          print(num, ". ", i)
          num += 1
          time.sleep(0.3)

        present = input("어떤 것을 선물할까? (숫자로 입력) ")
        print(animal_key[int(friend) - 1], "에게 ", my_pocket[int(present) - 1], "을(를) 선물했다!")
        time.sleep(0.5)
        animal[animal_key[int(friend) - 1]] += 5
        print(animal_key[int(friend) - 1], " 친밀도 +5")

        del my_pocket[int(present) - 1]


      # 2-3. 떄리기를 선택한 경우
      elif answer_animal_action == "3":
        print(animal_key[int(friend) - 1], ": 응..? 아야! 왜 그러는거야!")
        time.sleep(0.3)
        print(animal_key[int(friend) - 1], "을(를) 때렸다!")
        time.sleep(0.3)
        animal[animal_key[int(friend) - 1]] -= 1
        print(animal_key[int(friend) - 1], "친밀도 -1")
      time.sleep(0.5)

    # 3. 나무 흔들기를 선택한 경우
    elif answer_action == "3":
      result = random.choice(["100벨", "사과", "벌"])
      print("나무를 흔듭니다")
      time.sleep(0.5)
      print("응..?")
      time.sleep(0.5)

      # 100벨이 떨어질경우
      if result == "100벨":
        print("100벨이 떨어졌습니다!")
        my_bell += 100

      # 사과가 떨어질경우
      elif result == "사과":
        print("사과가 떨어졌습니다!")
        time.sleep(0.5)
        print("와~ 사과를 얻었어!")
        my_pocket.append("사과")

      # 벌이 나타날경우
      elif result == "벌":
        print("벌이 나타났습니다!")
        time.sleep(0.5)
        print("아야.. 벌에게 물렸어")
      time.sleep(0.5)

    # 4. 정보보기를 선택한 경우
    elif answer_action == "4":
      # 이름 출력
      print("- 이름: ", name)
      time.sleep(0.2)

      # 남은 벨 출력
      print("- 남은 벨: ", my_bell)
      time.sleep(0.2)

      # 주머니 출력
      if(len(my_pocket) == 0) :
        print("- 내 주머니: 비었음")
      else:
        print("- 내 주머니: ", my_pocket)
      time.sleep(0.2)

      # 주민 친밀도 출력
      num = 1
      for i in animal :
        print(num, ". ", i, ": ", animal[i])
        num += 1
        time.sleep(0.2)

    # 잘못된 입력을 했을경우
    else:
      print("잘못된 입력입니다. 다시 입력해주세요")
      time.sleep(0.5)