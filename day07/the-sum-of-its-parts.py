import re


def read_input(raw = False):
    file = "input.txt"
    return open(file).readlines() if raw else [re.findall(r'[A-Z]', _.strip()[5:]) for _ in open(file)]


def part_one():
    input = read_input()
    keys = set(re.findall(r'[A-Z]', ''.join([_.strip()[1:] for _ in read_input(True)])))
    graph = {k: set() for k in keys}
    [graph[right].add(left) for left, right in input]
    order = ""

    while len(graph) > 0:
        next_item = min([k for k, v in graph.items() if len(v) == 0])
        del graph[next_item]
        [v.discard(next_item) for k, v in graph.items()]
        order += next_item

    return order

def part_two_v1():
    input = read_input()
    keys = set(re.findall(r'[A-Z]', ''.join([_.strip()[1:] for _ in read_input(True)])))
    graph = {k: set() for k in keys}
    [graph[right].add(left) for left, right in input]
    
    task_time_table = {chr(_): _ - ord('A') + 61 for _ in range(ord('A'), ord('Z') + 1)}
    time = 0
    workers = {key: None for key in range(5)}

    while len(graph) > 0:
        # check worker's tasks for completion
        for worker in [(w, job) for w, job in workers.items() if job is not None]:
            w = worker[0]
            task, started = worker[1]
            if time >= started + task_time_table[task]:
                workers[w] = None
                del graph[task]
                [v.discard(task) for k, v in graph.items()]

        # get current tasks that are worked on
        curr_tasks = [job[0] for w, job in workers.items() if job is not None]

        # get next tasks
        tasks = [k for k, v in graph.items() if len(v) == 0 and k not in curr_tasks]

        # find free workers and assign jobs
        free_workers = [_ for _ in workers if workers[_] is None]
        for w in free_workers:
            if len(tasks) > 0:
                next_task = min(tasks)
                del tasks[tasks.index(next_task)]
                workers[w] = next_task, time

        time += 1

    return time - 1


print(part_one())
print(part_two_v1())
