from pagerank import transition_model, sample_pagerank, iterate_pagerank

corpus = {"1.html": {"2.html", "3.html"}, "2.html": {"3.html"}, "3.html": {"2.html"}}
page = "1.html"
damp = 0.85


transition_model(corpus, page, damp)
print(sample_pagerank(corpus, 0.85, 5000))
print(iterate_pagerank(corpus, 0.85))
