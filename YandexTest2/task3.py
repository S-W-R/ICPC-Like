import heapq

split_char = ' '
INPUT_FILE = 'input.txt'
OUTPUT_FILE = 'output.txt'

#with open(INPUT_FILE, encoding="utf8", mode='r') as i_file:
#    with open(OUTPUT_FILE, encoding='utf8', mode='w') as o_file:
#n = int(i_file.readline())

n = int(input())
heap = []
workers = {} #имя -> старт, имя
deleted_workers = {} #имя -> опыт, имя
workers_sum = 0
last_time = -1
for i in range(n):
    #raw_i = i_file.readline().split(split_char)
    raw_i = input().split(split_char)

    name, time = raw_i[0], int(raw_i[1])
    w = (time, name)

    if last_time == -1:
        last_time = time

    workers_sum += len(workers) * (time - last_time)

    if name in workers:
        worker_time, worker_name = workers.pop(name)
        exp = (time - worker_time)
        workers_sum -= exp
        deleted_workers[worker_name] = (exp, worker_name)
        oldest_time, oldest_name = heap[0]
        while oldest_name not in workers or oldest_time != workers[oldest_name][0]:
            heapq.heappop(heap)
            oldest_time, oldest_name = heap[0]

    else:
        if name in deleted_workers:
            worker_exp, worker_name = deleted_workers.pop(name)
            new_worker = (time - worker_exp, name)
            heapq.heappush(heap, new_worker)
            workers[name] = new_worker
            workers_sum += worker_exp
        else:
            heapq.heappush(heap, w)
            workers[name] = w

    oldest_time, oldest_name = heap[0]
    oldest_dif = workers_sum - 2 * (time - oldest_time)

    res = f"{oldest_name} {oldest_dif}"
    print(res)
    last_time = time

