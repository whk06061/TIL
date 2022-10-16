import heapq
q = []
food_times = [3,1,2]
for i in range(len(food_times)):
    heapq.heappush(q, (food_times[i], i+1))