import os
import re
import json
import pandas as pd

# make a new directory for the preprocessed data
dir_path = os.getcwd() + '/data'
os.makedirs(dir_path, exist_ok=True)

def preprocess_news_data(_dir, sub_dir):
    news_contents = []
    for sub_sub_dir in ['fake', 'real']:
        for folder in os.listdir(_dir + '/' + sub_dir + '/' + sub_sub_dir):
            news_content = {}
            news_content['id'] = re.findall(r'\d+', folder)[0]
            news_content['comments'] == ''
            print(folder)
            try:
                for file in os.listdir(_dir + '/' + sub_dir + '/' + sub_sub_dir + '/' + folder + '/tweets'):
                    try:
                        with open(_dir + '/' + sub_dir + '/' + sub_sub_dir + '/' + folder + '/tweets/' + file) as f:
                            file_content = json.load(f)
                            if news_content['comments'] != '':
                                news_content['comments'] += '::'
                            news_content['comments'] +=  + file_content['text'] + '<>' + file_content['created_at'] if file_content['in_reply_to_status_id'] is not None else ''
                    except Exception as e:
                        print('Error: ', e)
            except Exception as e:
                print('Error: ', e)

            news_contents.append(news_content)
    return news_contents

gossipcop_twitter_comments = preprocess_news_data('fakenewsnet_dataset', 'gossipcop')
gossipcop_twitter_comments_df = pd.DataFrame(gossipcop_twitter_comments)
gossipcop_twitter_comments_df.to_csv('data/gossipcop_no_ignore_comments.tsv', sep='\t', index=False)

politifact_news_contents = preprocess_news_data('fakenewsnet_dataset', 'politifact')
politifact_news_contents_df = pd.DataFrame(politifact_news_contents)
politifact_news_contents_df.to_csv('data/politifact_no_ignore_comments.tsv', sep='\t', index=False)


