# dowload_conference_papers
Placeholder for scripts to download conference papers.

Scripts for following conferences are available:
1. CVPR 2020 
2. ECCV 2020

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