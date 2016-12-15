import time
import os


def logger(expiration_time, file_path='log.txt'):  # expiration_time in days
    def wrapper(func):
        def replacement_function(*args, **kwargs):
            if os.path.exists(file_path) and (time.time() - os.path.getctime(file_path)) > expiration_time * 86400:
                os.remove(file_path)
                time.sleep(16)  # Sleep added to avoid default Windows tunneling(16 sec)

            with open(file_path, 'a') as log_file:
                log_file.write('Function {} called at {}!\n'.format(func.__name__, time.asctime()))
        return replacement_function
    return wrapper


@logger(1)
def summirize(x, y):
    return x + y

if __name__ == '__main__':
    print str(summirize(2, 3))