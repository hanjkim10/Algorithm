from collections import deque

def solution(new_id):
    # step 1
    new_id = new_id.lower()
    count = 0
    queue = deque()

    # step 2, 3
    for i in new_id:
        if '0' <= i <= '9' or 'a' <= i <= 'z' or i == '-' or i == '_' or i == '.':
            if i == '.':
                count += 1
                if count <= 1:
                    queue.append(i)
            else:
                count = 0
                queue.append(i)

    # step 4
    while queue:
        if queue[0] == '.':
            queue.popleft()
        elif queue[-1] == '.':
            queue.pop()
        else:
            break

    # step 5
    if not queue:
        queue.append('a')

    # step 6
    while len(queue) >= 16:
        queue.pop()

    # step 6
    while queue:
        if queue[-1] == '.':
            queue.pop()
        else:
            break

    # step 7
    while len(queue) <= 2:
        last = queue[-1]
        queue.append(last)

    answer = ''

    for i in queue:
        answer += i

    return answer