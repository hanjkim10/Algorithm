## 프로그래머스 폰켓몬

def solution(nums):
    pokemon = len(set(nums))

    if pokemon > len(nums) // 2:
        return len(nums) // 2
    elif pokemon < len(nums) // 2:
        return pokemon
    elif pokemon == len(nums) // 2:
        return pokemon