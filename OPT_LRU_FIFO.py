print("")
print('#############################################################################################')
print('#       Conducted by Springs Lau @ School of Computer Science and Engineering, BUAA         #')
print('#       Mar 24th, 2021, First Edition                                                       #')
print('#       MyEmail: lau@buaa.edu.cn    MyStudentID@BUAA: 19373345 Zhaoxun Liu                  #')
print('#############################################################################################')
print("")

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def show_axis():
    plt.xlim(0, 11)
    plt.xticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    plt.ylim(0, 100)
    plt.yticks([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
    for i in range(10):
        plt.plot([0, 11], [(i+1)*10, (i+1)*10], linewidth='1', color='aliceblue')
        plt.plot([i+1, i+1], [0, 100], linewidth='1', color='aliceblue')


def show_graph(opt_faults, lru_faults, fifo_faults):
    show_axis()
    ln1, = plt.plot(x, opt_faults, color='cornflowerblue', marker='o', markersize='3')
    ln2, = plt.plot(x, lru_faults, color='gold', marker='^', markersize='3')
    ln3, = plt.plot(x, fifo_faults, color='firebrick', marker='D', markersize='3')
    plt.legend([ln1, ln2, ln3], ['OPT', 'LRU', 'FIFO'])
    for i in range(10):
        plt.text(i + 1, opt_faults[i] + 1, str(opt_faults[i]), ha='center', va='bottom', fontsize='8')
        plt.text(i + 1, lru_faults[i] + 1, str(lru_faults[i]), ha='center', va='bottom', fontsize='8')
        plt.text(i + 1, fifo_faults[i] + 1, str(fifo_faults[i]), ha='center', va='bottom', fontsize='8')
    plt.show()

page_visit_list = [0, 9, 8, 4, 4, 3, 6, 5, 1, 5,
                   0, 2, 1, 1, 1, 1, 8, 8, 5, 3,
                   9, 8, 9, 9, 6, 1, 8, 4, 6, 4,
                   3, 7, 1, 3, 2, 9, 8, 6, 2, 9,
                   2, 7, 2, 7, 8, 4, 2, 3, 0, 1,
                   9, 4, 7, 1, 5, 9, 1, 7, 3, 4,
                   3, 7, 1, 0, 3, 5, 9, 9, 4, 9,
                   6, 1, 7, 5, 9, 4, 9, 7, 3, 6,
                   7, 7, 4, 5, 3, 5, 3, 1, 5, 6,
                   1, 1, 9, 6, 6, 4, 0, 9, 4, 3]


def opt_to_replace(i, frame_usage):
    future_list = page_visit_list[i+1:]
    to_replace = frame_usage[0]
    next_use = 0
    for page in frame_usage:
        if page in future_list:
            if future_list.index(page) > next_use:
                to_replace = page
                next_use = future_list.index(page)
        else:
            to_replace = page
            break
    return to_replace


def opt(frame_num):
    page_fault = 0
    frame_usage = []
    to_replace = 0
    for i in range(len(page_visit_list)):
        page = page_visit_list[i]
        if page in frame_usage:
            to_replace = opt_to_replace(i, frame_usage)
            continue
        page_fault = page_fault + 1
        if len(frame_usage) < frame_num:
            frame_usage.append(page)
            to_replace = opt_to_replace(i, frame_usage)
            continue
        frame_usage[frame_usage.index(to_replace)] = page
        to_replace = opt_to_replace(i, frame_usage)
    return page_fault


def lru(frame_num):
    page_fault = 0
    frame_usage = []
    for page in page_visit_list:
        if page in frame_usage:
            frame_usage.remove(page)
            frame_usage.append(page)
            continue
        page_fault = page_fault + 1
        if len(frame_usage) < frame_num:
            frame_usage.append(page)
            continue
        frame_usage.remove(frame_usage[0])
        frame_usage.append(page)
    return page_fault


def fifo(frame_num):
    page_fault = 0
    frame_usage = []
    for page in page_visit_list:
        if page in frame_usage:
            continue
        page_fault = page_fault + 1
        if len(frame_usage) < frame_num:
            frame_usage.append(page)
            continue
        frame_usage.remove(frame_usage[0])
        frame_usage.append(page)
    return page_fault


if __name__ == '__main__':
    opt_faults, lru_faults, fifo_faults = [], [], []
    for i in range(10):
        opt_faults.append(opt(i+1))
        lru_faults.append(lru(i+1))
        fifo_faults.append(fifo(i+1))
    show_graph(opt_faults, lru_faults, fifo_faults)
    print(opt_faults)
    print(lru_faults)
    print(fifo_faults)
    print('Done.')