# Mission_to_Mars
Our goal is using splinter and BeautifulSoup to scrape webpages and return the display on a webpage using MongoDB and Flask

#Scraping Mars Data
We first wrote in a jupyter notebook to test our code. 
we imoported the dependencies with the chrome dirver and and set up my browser to open the webpages I needed to to some scraping on.
1st website:
NASA Mars News: title and text of most recent article
Used beautiful Soup as soup to parse through the HTML and use find_all() whcih gave us lists so we indexed the first item and took the text of that

2nd website:
Jet Propolsion Laboratory's Mars page:
we wanna access the full size image page with required us to jump two further pages whcich required using browser.click_link_by_partial_text().
Used Beautiful Soup as soup: soup.find_all() and a.[''] to find the image path which i combined with the url to get the full size image.

3rd website:
Mars Weather Twitter Account:
Used Beautiful Soup as soup to parse through the HTML and use find_all() which gave us lists so we indexed the first iten and took the text of that

4rth:
Scraping Mars facts from the Scrape Facts website
The data is a table so we are using pandas as pd instead of Beuatiful Soup to scrape using pd.read_html() and took the second returned table that had all the data I needed, I then renamed the columns and set the index before converting that data frame into an HTML table with df.html()

5th :
USGS Astrogeology
Used BeautifulSoup as Soup to seach for hemispheres titles

Once done working on jupyter notebook, all the code was transferred to a Python file where we implemented  all the code in a function 
Then we used flask to call the function, and upload the data the our MongoDB server and then display that data on a webpage
                                                     
