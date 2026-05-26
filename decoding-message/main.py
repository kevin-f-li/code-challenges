import requests
from bs4 import BeautifulSoup

def decode_message(doc_url):
    html_text = requests.get(doc_url).text

    soup = BeautifulSoup(html_text, 'html.parser')
    tags = soup.select('tr > td')

    values = [tag.text.partition('░█')[0] for tag in tags]
    values = values[3:]
    
    points = []

    for i in range(1, len(values) - 1):
        if values[i].startswith(('░','█')):
            x = int(values[i - 1])
            character = values[i]
            y = int(values[i + 1])

            points.append((x, y, character))
    
    max_x = max(x for x, y, c in points)
    max_y = max(y for x, y, c in points)

    grid = [[' ' for _ in range(max_x + 1)] for _ in range(max_y + 1)]

    for x, y, character in points:
        grid[y][x] = character

    for row in grid:
        print(''.join(row))

if __name__ == "__main__":
    doc_url = "https://docs.google.com/document/d/e/2PACX-1vSvM5gDlNvt7npYHhp_XfsJvuntUhq184By5xO_pA4b_gCWeXb6dM6ZxwN8rE6S4ghUsCj2VKR21oEP/pub"
    decode_message(doc_url)