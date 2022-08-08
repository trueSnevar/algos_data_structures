from typing import List, Tuple

def get_distance(street_length: int, street_map: List[int]) -> List[int]:
    result = [0] * street_length
    curr_dist = None
    for house_idx in range(street_length):
        if street_map[house_idx] == 0:
            curr_dist = 0
            for back_idx in range(house_idx, -1, -1):
                if curr_dist <= result[back_idx]:
                    result[back_idx] = curr_dist
                    curr_dist += 1
                else:
                    break
            curr_dist = 0
        else:
            curr_dist += 1
            result[house_idx] = curr_dist
    return result   

def read_input() -> Tuple[int, List[int]]:
    street_length = int(input())
    street_map = list(map(int, input().strip().split()))
    return street_map

street_map = read_input()
print(" ".join(map(str, get_distance(street_length, street_map))))