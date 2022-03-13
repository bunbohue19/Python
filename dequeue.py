from collections import deque
waiting_list = deque()
print(waiting_list)

waiting_list.append('Ahmed')
waiting_list.append('Fred')
waiting_list.append('ronald')
waiting_list.append('Ibrahim')

print(waiting_list)

waiting_list.popleft()
print(waiting_list)

waiting_list.clear()
print(waiting_list)
