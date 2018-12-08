import time


class ContextManager:
    def __enter__(self):
        start_time = time.time()
        print('Начало работы программы: {}'.format(time.ctime(start_time)))
        return start_time

    def __exit__(self, type, value, traceback):
        end_time = time.time()
        print('Окончание работы программы: {}'.format(time.ctime(end_time)))
        sum_time = end_time - start_time
        print('Время работы программы: {} с.'.format(sum_time))


def calculate_num():
    print('Для вычисления по формуле (x*y + 18)/2 введите два числа')
    x = float(input('Введите первое число: '))
    y = float(input('Введите второе число: '))
    total_num = (x*y + 18)/2
    print('Результат вычисления: {}'.format(total_num))
    return total_num


if __name__ == "__main__":
    with ContextManager() as start_time:
        calculate_num()
