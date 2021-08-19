from pygooglenews import GoogleNews

# default GoogleNews instance
gn = GoogleNews(lang = 'en', country = 'UK')
topic = "Female Directors"
top_news = gn.search(topic)
#top_news  gn.top_news()
print(type(top_news))
i = 0
for key in top_news :
    print(key)
    #print(type(key))
    #print("*** \n {} \n ***".format(top_news['entries']))
    entry = top_news['entries']
    i += 1
#print(entry)
print(i)
#print(type(entry)) # list
# print(entry[0])
#print(len(entry)) # 38
#print(type(entry[0]))
#for key in entry[0] :
#    print(key)

# title
#title_detail
#links
#link
#id
#guidislink
#published
#published_parsed
#summary
#summary_detail
#source
#sub_articles

for k in range(0, len(entry)) :
    print(entry[k]['title'])
    # print(entry[i]['title_detail'])
#print(i)
