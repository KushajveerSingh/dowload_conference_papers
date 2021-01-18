import pandas as pd
import os
from urllib.request import urlretrieve
from multiprocessing import Pool
from tqdm import tqdm
from functools import partial

df = pd.read_csv('csv_files/iclr2021.csv')
oral, spotlight, poster = [], [], []
oral_c, spotlight_c, poster_c = 1000, 1000, 1000

for _, row in df.iterrows():
    url = row['url'].replace('forum', 'pdf', 1)
    name = row['title'].replace(' ', '_').replace('/', '_').replace('?', '_').replace(':', '_')+'.pdf'
    cat = row['final_decision']

    if cat == "Accept (Oral)":
        name = f"{oral_c}_oral_" + name
        oral.append([name, url])
        oral_c += 1
    elif cat == "Accept (Spotlight)":
        name = f"{spotlight_c}_spotlight_" + name
        spotlight.append([name, url])
        spotlight_c += 1
    elif cat == "Accept (Poster)":
        name = f"{poster_c}_poster_" + name
        poster.append([name, url])
        poster_c += 1

assert len(oral) == 53
assert len(spotlight) == 114
assert len(poster) == 693


def download_papers(info, save_path):
    save_path = os.path.join(save_path, info[0])
    urlretrieve(info[1], save_path)


def setup(cat: str):
    save_path = os.path.join(SAVE_PATH, cat)
    os.makedirs(save_path, exist_ok=True)

    print(f'Started downloading {cat} papers')
    func = partial(download_papers, save_path=save_path)

    if cat == "oral":
        info = oral
    elif cat == "spotlight":
        info = spotlight
    elif cat == "poster":
        info = poster

    with Pool(processes=PROCESSES) as p:
        with tqdm(total=len(info)) as pbar:
            for i, _ in enumerate(p.imap_unordered(func, info)):
                pbar.update()


if __name__ == "__main__":
    SAVE_PATH = "../../ICLR"  # where to save the papers
    PROCESSES = 8  # number of threads on your CPU

    os.makedirs(SAVE_PATH, exist_ok=True)

    # comment out the sections for which you don't want to download papers
    setup('oral')
    setup('spotlight')
    setup('poster')
