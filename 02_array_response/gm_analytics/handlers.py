import logging

def get_user_info(org, repo, username):
    logging.debug('org=%s repo=%s username=%s',org, repo, username)
    return {"user_info": username}

def get_commits_info(org, repo, username, time_range=30):
    logging.debug('org=%s repo=%s username=%s',org, repo, username)
    logging.debug('time_range=%s', time_range)
    return [{'commits_count': 10, 'yyyymmdd_date': '20180101'},
            {'commits_count': 10, 'yyyymmdd_date': '20180102'}]
