import os
import time
from multiprocessing import Pool
from PIL import Image

BASE = os.path.dirname(os.path.abspath(__file__))
INPUT = os.path.join(BASE, "img")
OUTPUT = os.path.join(BASE, "processed")
SIZE = (800, 600)


def process(filename):
    img = Image.open(os.path.join(INPUT, filename))
    img = img.rotate(-90, expand=True)
    img = img.resize(SIZE, Image.LANCZOS)
    img = img.convert("L")
    img.save(os.path.join(OUTPUT, f"out_{filename}"))


def main():
    os.makedirs(OUTPUT, exist_ok=True)
    files = os.listdir(INPUT)

    start = time.time()
    for f in files:
        process(f)
    seq_time = time.time() - start

    start = time.time()
    with Pool() as pool:
        pool.map(process, files)
    par_time = time.time() - start

    print(f"Последовательно: {seq_time:.4f} сек")
    print(f"Параллельно:     {par_time:.4f} сек")


if __name__ == "__main__":
    main()