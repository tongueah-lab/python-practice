# 위 수식 그대로, 플레이어 선공 → 몬스터 사망 확인 → 몬스터 공격 → 플레이어 사망 확인
player_hp = 100
monster_hp = 80
turn = 0
print("=== RPG 전투 시작! ===")
print("플레이어 HP:", player_hp, "| 몬스터 HP:", monster_hp)
print()


# 미니 RPG 전투
# 참일 때까지 반복하기
while True:
    
    # 턴 출력하기
    turn += 1
    print(f"--- {turn}턴 ---")

    # 먼저 플레이어가 공격하면 몬스터 피 깎임
    p_damage = 15 + (turn * 7 + 3) % 11
    monster_hp -= p_damage
    print(f"플레이어 공격! 데미지: {p_damage} | 몬스터 HP: {monster_hp}")
    
    # 몬스터 피가 0 이하이면 즉시 종료
    if monster_hp <= 0:
        print()
        print(f"플레이어 승리! ({turn}턴 만에 승리)")
        break
    
    # 이어서 몬스터가 공격하면 플레이어 피 깎임
    m_damage = 10 + (turn * 11 + 5) % 11
    player_hp -= m_damage
    print(f"몬스터 공격! 데미지: {m_damage} | 플레이어 HP: {player_hp}")

    # 플레이어 피가 0 이하이면 종료
    if player_hp <= 0:
        print()
        print("몬스터 승리... (플레이어 패배)")
        break

    # 줄 바꿈
    print()