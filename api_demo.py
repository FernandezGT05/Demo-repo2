import requests
import json

isbn="9781501175466"
url=f"https://www.googleapis.com/books/v1/volumes?q=isbn:{isbn}"

def get_book_info(isbn):
    response=requests.get(url)
    print(f"Status code: {response.status_code}\n")
    if response.status_code!=200:
        return False
    book_data=response.json()
    print(json.dumps(book_data,indent=5))
    if 'items'not in book_data:
        return None
    volume_data=book_data['items'][0]['volumeInfo']
    return volume_data
book_info=get_book_info(isbn)

if book_info:
    print("----Book Info----")
    print(f"Title: {book_info['title']}")
    print(f"Author: {book_info['authors']}")
    print(f"Published Date: {book_info['publishedDate']}")
    print(f"Description: {book_info['description']}")
    print(f"Categories: {book_info['categories']}")

elif book_info==False:
    print("Error")
elif  book_info==None:
    print("Book not found")

