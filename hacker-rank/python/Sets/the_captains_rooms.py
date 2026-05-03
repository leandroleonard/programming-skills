n = int(input())

rooms = list(map(int, input().split()))

set_rooms = set(rooms)

for i in set_rooms:
    rooms.remove(i)
    
print(set_rooms.difference(set(rooms)).pop()) 