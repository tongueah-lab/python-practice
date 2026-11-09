# while game_over == 0 루프에서 current_room으로 분기
hp = 100
has_key = 0
current_room = 1
game_over = 0

# 시작 시 미니 텍스쳐 출력하기
print("=== 미니 텍스트 어드벤처 ===")
print("당신은 신비한 던전에 들어왔습니다...")
print("HP:", hp)

# 게임 오버가 될 때까지 반복하기
while game_over == 0:
    print()
    if current_room == 1:
        # 방 1(시작의 방) 출력하기
        print("--- 방 1: 시작의 방 ---")
        print("두 개의 문이 보입니다.")
        print("(1) 왼쪽 문  (2) 오른쪽 문")
        
        # 선택 입력받기
        num = int(input())

        # 1번을 선택했으면 방 2로 가기
        if num == 1:
            print("왼쪽 문을 열고 조심스럽게 들어갑니다.")
            current_room = 2
        # 2번을 선택했으면 hp-=20하기
        elif num == 2:
            hp -= 20
            print("오른쪽 문에 함정이 있었습니다! HP -20")
            print("HP:", hp)
            # 남은 체력이 0이하면 종료
            if hp <= 0:
                print("체력이 다했습니다... 게임 오버!")
                game_over = 1
            # 아니면 방 2로 가기
            else:
                current_room = 2
        # 그 외면 1, 2 선택하라고 출력하기
        else:
            print("1 또는 2를 선택하세요.")
    
    elif current_room == 2:
        # 방 2(보물의 방) 출력하기
        print("--- 방 2: 보물의 방 ---")
        print("낡은 상자가 하나 있습니다.")
        print("(1) 상자 열기  (2) 그냥 지나가기")

        num = int(input())
        # 1번을 선택하면 키 획득하고 방 3으로 가기
        if num == 1:
            has_key = 1
            print("상자에서 열쇠를 발견했습니다!")
            current_room = 3
        # 2번을 선택하면 상자 무시하고 방 3으로 가기
        elif num == 2:
            print("상자를 무시하고 지나갑니다.")
            current_room = 3
        # 그 외는 1, 2 선택하라고 출력하기
        else:
            print("1 또는 2를 선택하세요.")

    elif current_room == 3:
        # 방 3(최종 방) 출력하기
        print("--- 방 3: 최종 방 ---")
        print("거대한 잠긴 문이 보입니다.")
        # 열쇠가 있다면 열쇠로 문을 열기
        if has_key == 1:
            print("열쇠로 문을 열었습니다!")
            # 빈 줄
            print()
            # 축하 인사, 체력 출력 후 종료
            print("축하합니다! 던전에서 탈출했습니다!")
            print(f"남은 HP: {hp}")
            game_over = 1
        # 그 외 방법 출력하기
        else:
            print("문이 잠겨 있습니다! 열쇠가 필요합니다.")
            print("(1) 돌아가기(방2)  (2) 문 부수기(HP-50)")

            num = int(input())
            # 1을 선택하면 방 2로 돌아가기
            if num == 1:
                print("방 2로 돌아갑니다.")
                current_room = 2
            # 2를 선택하면 체력 -50되기
            elif num == 2:
                hp -= 50
                print("문을 부쉈습니다! HP -50")
                print("HP:", hp)
                # 체력이 0이하면 게임오바 후 종료
                if hp <= 0:
                    print("체력이 다했습니다... 게임 오버!")
                    game_over = 1
                # 아니면 빈 줄
                else:
                    print()
                    # 탈출 후 종료
                    print("문을 부수고 탈출했습니다!")
                    print(f"남은 HP: {hp}")
                    game_over = 1
            # 그 외 1 또는 2 선택하기
            else:
                print("1 또는 2를 선택하세요.")
