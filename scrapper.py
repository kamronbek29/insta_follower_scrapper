import csv

import instaloader

iloader = instaloader.Instaloader()


USERNAME = ''
PASSWORD = ''
USERNAME_TO_SCRAPE = ''

print('Getting followers from {}'.format(USERNAME_TO_SCRAPE))
file_with_followers = '{}.csv'.format(USERNAME_TO_SCRAPE)

iloader.login(USERNAME, PASSWORD)
scrape_profile_info = instaloader.Profile.from_username(iloader.context, USERNAME_TO_SCRAPE)
main_followers = scrape_profile_info.followers
count = 0
total = 0

with open(file_with_followers, 'a', newline='') as csv_file_followers:
    csv_writer = csv.writer(csv_file_followers)
    csv_writer.writerow(['user_id', 'username', 'fullname', 'follower_count', 'following_count'])
    for person in scrape_profile_info.get_followers():
        try:
            total += 1
            user_id = person.userid
            username = person.username
            fullname = person.full_name
            follower_count = person.followers
            following_count = person.followees

            csv_writer.writerow([user_id, username, fullname, follower_count, following_count])

        except Exception as e:
            print(e)

print('Scrapped {0} followers from {1}'.format(total, USERNAME_TO_SCRAPE))
