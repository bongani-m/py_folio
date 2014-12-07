def page_filter(pages, type):
    filtered_pages = []
    for page in pages:
        if page['type'] == type:
            filtered_pages.append(page)
    return filtered_pages


def return_page(pages, page):
    page = pages.get('hello-world')
    return page


def tag_filter(pages, tag):
    filtered_pages = []
    for page in pages:
        if tag in page['tags']:
            filtered_pages.append(page)
    return filtered_pages


def return_tag(pages, tagProp):
    return pages.values()
