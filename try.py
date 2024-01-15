import gensim.downloader as dl
model = dl.load("word2vec-google-news-300")
vocab = model.index_to_key
# Print the first 10 words in the vocabulary
w_list = ["cat", "dog", "computer", "house", "tree"]
for w in w_list:
    print(w, "\n20 most similar:\n", model.most_similar(w, topn=20))

