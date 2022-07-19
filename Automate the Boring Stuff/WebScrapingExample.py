import bs4, requests

# only for CSS sites
def getAmazonPrice(productUrl):
    res = requests.get(productUrl)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html parser')
    elems = soup.select(# CSS from site)
    return elems[0].text.strip()

