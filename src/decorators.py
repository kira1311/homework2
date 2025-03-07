import functools


def log(filename=None):
    '''Будет автоматически логировать начало и конец выполнения функции, а также ее результаты или возникшие ошибки.
    Декоратор должен принимать необязательный аргумент filename, который определяет, куда будут записываться логи'''
    def decorator(func):
        '''Декоратор получает имя файла выводит результат в этот файл
        или выводит в консоль, определяет ошибку при возникновении,
        выводит информацию о ней'''
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                log_message = f"{func.__name__} ok"
                if filename:
                    with open(filename, 'a') as f:
                        f.write(log_message + "\n")
                else:
                    print(log_message)
                return result

            except Exception as e:
                error_message = (f"{func.__name__} error: {type(e).__name__}."
                                 f" Inputs: {args}, {kwargs}")
                if filename:
                    with open(filename, 'a') as f:
                        f.write(error_message + '\n')
                else:
                    print(error_message)

                raise

        return wrapper
    return decorator


@log(filename="mylog.txt")
def my_function(x, y):
    '''Функция возвращает сумму чисел'''
    return x + y


@log()
def error_function(x, y):
    '''Функция возвращает делениe чисел'''
    if y == 0:
        raise ValueError
    return x / y
