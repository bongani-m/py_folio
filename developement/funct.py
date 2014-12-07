##################
## FUNCTIONS #####
##################


## takes in the pages and a metadeta type that you specify and returns
## matching pages
def page_filter(pages, type):
    filtered_pages = []
    for page in pages:
        if page['type'] == type:
            filtered_pages.append(page)
    return filtered_pages


## grabs that particular page
def return_page(pages, page):
    page = pages.get('hello-world')
    return page


## filters and return posts matching blog tag
def tag_filter(pages, tag):
    filtered_pages = []
    for page in pages:
        if tag in page['tags']:
            filtered_pages.append(page)
    return filtered_pages


#returns list of tags
def return_tag(pages, tagProp):
    return pages.values()
