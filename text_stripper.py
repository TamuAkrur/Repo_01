from googlesearch import search
# pip install beautifulsoup4
# pip install google

# to search
query = "The day that never comes"

for j in search(query, tld="co.in", num=10, stop=10, pause=2):
    print(j)
