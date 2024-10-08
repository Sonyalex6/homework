from multiprocessing import Pool
import datetime
def read_info(fname):
    all_data = []
    with open(fname, 'r') as f:
        line = f.readline()
        while line:
            all_data.append(line)
            line = f.readline()
def main_x1():
    fnames = [f'file {_}.txt' for _ in range(1, 5)]
    time = datetime.datetime.now()
    for fname in fnames:
        read_info(fname)
    print('main_x1:', datetime.datetime.now() - time)
def main_x(np=4):
    fnames = [f'file {_}.txt' for _ in range(1, 5)]
    time = datetime.datetime.now()
    with Pool(processes=4) as pool:
        pool.map(read_info, fnames)
    print(f'main_x{np}', datetime.datetime.now() - time)
if __name__ == '__main__':
    main_x1()
    main_x(np=2)
    main_x(np=4)