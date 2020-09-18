import os
from pathlib import Path
from urllib.request import urlretrieve
from bs4 import BeautifulSoup
import pandas as pd
from fastcore.utils import parallel

path, soups = Path('html_extra/cvpr_2020'), []
for file in sorted(os.listdir(path)): soups.append(BeautifulSoup(open(path/file), 'html.parser'))

titles, urls, index = [], [], 1001
for soup in soups:
    query = soup.findAll('dt', attrs={'class':'ptitle'})
    for q in query:
        # extract title
        title = str(index) + '_' + q.a.text.replace(' ', '_').replace('/', '_').replace('?','_').replace(':','_')+'.pdf'
        titles.append(title)
        index += 1
        
        # extract url
        url = 'https://openaccess.thecvf.com/content_CVPR_2020/papers/' + q.a['href'][23:-4] + 'pdf'
        urls.append(url)

assert len(titles) == len(urls)
info = list(zip(titles, urls))

# save results to csv file
df = pd.DataFrame(info, columns=['title', 'url'])
df.to_csv('csv_files/cvpr2020.csv', index=False)

def download_papers(info):
    save_path = '/home/kushaj/Desktop/TODO/cvpr2020'
    save_path = os.path.join(save_path, info[0])
    urlretrieve(info[1], save_path)

if __name__ == "__main__": parallel(download_papers, info, n_workers=24, progress=True)