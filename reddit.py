import praw

class reddit:
    reddit_client_id="nEQNt8A0EThlWQ"
    reddit_client_secret="Fa2OlDF3TyXvRx9xxvY-YU09UNA"
    reddit_user_agent="testscript by /u/Huge_Requirement v1.0"
    redirect_uri="http://127.0.0.1"
    reddit_password='RbWtUh@##'
    reddit_username="Huge_Requirement"
    subreddit = None
    reddit = None

    def reddit_init(self, subreddit):
        self.reddit = praw.Reddit(client_id=self.reddit_client_id,
                     client_secret=self.reddit_client_secret,
                     user_agent=self.reddit_user_agent,
                     redirect_uri=self.redirect_uri,
                     password=self.reddit_password,
                     username=self.reddit_username)
        self.subreddit = self.reddit.subreddit(subreddit)

    def get_post(self):
        posts = list(self.subreddit.hot(limit=12))
        return posts
