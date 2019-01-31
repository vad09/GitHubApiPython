
# coding: utf-8

# In[21]:


import urllib.request as urllib
import simplejson as json
class GithubRepositories:
    #Getting the github repositories url
    def __init__(repos):
          response = urllib.urlopen('https://api.github.com/users/vad09/repos')
          data = response.read().decode("utf-8")
          #print(data)
          repos.data = json.loads(data) 
          #print(repos.data)
          repos.index = len(repos.data)
          #print(repos.index)
    def __iter__(repos):
        return repos

    def __next__(repos):
        
        if repos.index == 0:
            raise StopIteration
        repos.index = repos.index-1
        return repos.data[repos.index]

repository = GithubRepositories()
#print(repository.index)
for data in repository:
    print(data['name'])    

