# dowload_conference_papers
Placeholder for scripts to download conference papers.

Scripts for following conferences are available:
* [ICLR 2021](#ICLR-2021)
* ECCV 2020
* CVPR 2020 

### ICLR 2021
Thanks to [Sergey Ivanov](https://twitter.com/SergeyI49013776) for providing a csv file containing all ICLR papers with their urls. Original source of file [link](https://twitter.com/sergeyi49013776/status/1326218056088039425?lang=en). I have copied the file to [scripts/csv_files/iclr2021.csv](scripts/csv_files/iclr2021.py).

[scripts/iclr_2021.py](scripts/iclr_2021.py) is used to download the papers. Modify the `__main__` function as per your needs.

```python
SAVE_PATH = "../../ICLR"  # where to save the papers
PROCESSES = 8  # number of threads on your CPU

os.makedirs(SAVE_PATH, exist_ok=True)

# comment out the sections for which you don't want to download papers
setup('oral')
setup('spotlight')
setup('poster')
```

The papers are sorted by their rating. The final directory structure is
```
ICLR
├── oral
    ├── ... 
├── poster
    ├── ...
└── spotlight
    ├── ...
```

Final download size is 3.8 GB.

## Old

For every conference, corresponding csv files are also provided in **scripts/csv_files**.

To run the scripts use `python scripts/cvpr2020.py`. The external dependencies of the script are:
1. pandas (used to save csv file)
2. bs4 (used to convert html files to `BeautifulSoup` object for easier operation)
3. fastcore (this is only used to download the papers as it provides a progress bar during the download)

You can replace the fastcore dependency with python `multiprocessing` by using the following code

```python
from multiprocessing import Pool
pool = Pool(processes=12)
pool.map(download_papers, info)
```

Things to modify in the scripts
1. `df.to_csv('csv_files/cvpr2020.csv', index=False)`. You can specify a new location to save the csv file.
2. `save_path = '/home/kushaj/Desktop/TODO/cvpr2020'` in `download_papers`. This is the base path where the papers would be saved.
3. `parallel(download_papers, info, n_workers=24, progress=True)`. Change `n_workers=24` to the number of threads on your CPU.

By default, all the papers are saved using a 4-digit number as prefix starting from 1001. This is done so that I can later easily sort the papers. Also, some punctuations in the paper titles `[' ', '/', '?', ':']` are replaced with `'_'` (as these can cause some errors).