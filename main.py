import create_iamge, imgur, reddit


def title_process(title):
    number_of_spaces = 0
    index = 0
    numbers = {
        "1": "one",
        "2": "two",
        "3": "three",
        "4": "four",
        "5": "five",
        "6": "six",
        "7": "seven",
        "8": "eight",
        "9": "nine",
        "0": "zero",
    }
    for key, value in numbers.items():
        title = title.replace(key, value)
    for i in title:
        if i == " ":
            number_of_spaces += 1
        if number_of_spaces % 8 == 0 and number_of_spaces > 0:
            title = title[:index] + "\n" + title[index + 1 :]
            number_of_spaces += 1

        index += 1
    return title


def process():
    c = 0
    subreddits = ["showerthoughts", "themonkeyspaw"]
    print("0. shower thoughts \n1. the monkeys paw")
    subreddit = subreddits[int(input("Enter subreddit: "))]
    reddit_obj = reddit.reddit()
    imgur_obj = imgur.imgur()
    create_iamge_obj = create_iamge.create_image()
    reddit_obj.reddit_init(subreddit)
    imgur_obj.imgur_init()
    title = reddit_obj.get_post()
    for i in title:
        print(f"{c}: {i.title}")
        c += 1
    post_index = (input("Which one: ")).split(",")
    post_index = list(map(lambda x: int(x), post_index))
    for x_position in post_index:
        title1 = title_process(title[x_position].title)
        # print(title)
        create_iamge_obj.create_image_and_save(title1, subreddit)
        imgur_obj.upload_fking_image()


process()
