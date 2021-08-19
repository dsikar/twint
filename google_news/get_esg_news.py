def print_topic_headlines(topic) :
    """
    Print google news headlines for topic
    Input
        topic: string
    Output
        none
    Example
    print_topic_headlines("Female directors")
    """
    from pygooglenews import GoogleNews

    # default GoogleNews instance
    gn = GoogleNews(lang = 'en', country = 'UK')

    news = gn.search(topic)
    entry = news['entries']

    print("***** Headlines found for topic: : {} *****".format(topic))
    for k in range(0, len(entry)) :
        print(entry[k]['title'])

# open file

# print_topic_headlines("Mental health")
# exit()
f = open("esg_topics.txt")
for line in f :
    #print(line.strip())
    topic = line.strip()
    # print(topic)
    print_topic_headlines(topic)

