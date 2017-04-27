#!/usr/bin/env python3

import praw

def connect(client_file):
    """
    Reddit account connection.
    @param client_file: path of file with client_id, client_secret and 
    user_agent (one per line)
    @return Reddit.subreddit object
    """
    with open(client_file, 'r') as f:
        client = f.readlines()
    try:
        client_id, client_secret, user_agent = [i.strip() for i in client]
    except ValueError:
        print('File should contain client_id (new line) client_secret (new'
              'line) user_agent')

    r = praw.Reddit(client_id=client_id,
                    client_secret=client_secret,
                    user_agent=user_agent)
    return r.subreddit('unixporn')

def get_posts(sub, max_posts=1000):
    """
    Get every post and save tags and counts in a dictionary
    @param sub: subreddit object from connect function.
    @param max_posts: limit of posts
    @return: tags: dictionary with each found tag and its count
    """
    tags_list = []
    for post in sub.new(limit=max_posts):
        try:
            tags_list.append(post.title.split('[')[1].split(']')[0].lower())
            # !!! add more stuff. maybe a class not a dict
        except IndexError:
            pass
    tags = dict.fromkeys(set(tags_list))
    for i in set(tags_list):
        tags[i] = tags_list.count(i)

    return tags

if __name__ == '__main__':
    sub = connect('client')
    tags = get_posts(sub)
    # !!! to implement: save to file
    print(tags)
