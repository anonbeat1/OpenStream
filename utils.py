def get_url_from_link(link):
    try:
        username = link.split('/')[-1]
        return username
    except Exception as e:
        print("An error occurred while getting username",e)