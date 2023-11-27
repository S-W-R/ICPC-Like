class Worker:
    def __init__(self, index, height):
        self.index = index
        self.height = height
        self.weight = 0

    def __str__(self):
        return f'W: i:{self.index} h:{self.height} w:{self.weight}'


if __name__ == '__main__':
    count = int(input())
    workers = [Worker(x[1], int(x[0])) for x in
               zip(input().split(' '), range(count))]
    workers_dynamic = sorted(workers, key=lambda x: x.index, reverse=True)
    for i in range(len(workers_dynamic)):
        worker = workers_dynamic[i]
        targetWorker = None
        for j in range(i):
            assignedWorker = workers_dynamic[i - j - 1]
            if assignedWorker.height >= worker.height:
                targetWorker = assignedWorker
                break
        if targetWorker is None:
            targetWorker = worker
        worker.weight = targetWorker.weight + 1
    answer = ''
    for worker in workers:
        answer += f'{worker.weight} '
    print(answer[:-1])
