import os
import requests
from urllib.request import urlretrieve
from bs4 import BeautifulSoup
import pandas as pd
from fastcore.utils import parallel
from multiprocessing import Pool

# get html
url = 'https://www.ecva.net/papers.php'
html = requests.get(url).text

start_index = html.index(r"""
<dt class="ptitle"><br>
<a href=papers/eccv_2020/papers_ECCV/html/267_ECCV_2020_paper.php>
""")

end_index = html.index(r"""
</dl> </div>
	</div>


	<!-- ECCV 2018 -->
""")

html = html[start_index:end_index]
soup = BeautifulSoup(html, 'html.parser')

# extract title and url
query1 = soup.findAll('dt', attrs={'class':'ptitle'})
query2 = soup.findAll('dd')

index = 1001
titles = []
for q in query1:
    title = str(index)+'_'+q.a.text[1:-1].replace(' ', '_').replace('/', '_').replace('?','_').replace(':','_')+'.pdf'
    titles.append(title)
    index += 1

urls = []
for i,q in enumerate(query2):
    if i%2==0: continue
    url = 'https://www.ecva.net/' + q.a['href']
    urls.append(url)

assert len(titles) == len(urls)
info = list(zip(titles, urls))

# save results to a csv file
df = pd.DataFrame(info, columns=['title', 'url'])
df.to_csv('csv_files/eccv2020.csv', index=False)

def download_papers(info):
    save_path = '.'
    save_path = os.path.join(save_path, info[0])
    urlretrieve(info[1], save_path)

if __name__ == '__main__':
    # pool = Pool(processes=12)
    # pool.map(download_papers, info)
    parallel(download_papers, info, n_workers=24, progress=True)