import os
import random
import re
import sys
import numpy as np

DAMPING = 0.85
SAMPLES = 10000


def main():
    
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages


def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """
    
    consp = (1 - damping_factor)/len(corpus)
    final_prob ={} 
    for key in corpus:
        final_prob[key] = consp
    for element in corpus[page]:
        if len(corpus[page]) != 0:
            final_prob[element] += damping_factor * (1/len(corpus[page]))

    if len(corpus[page]) == 0:
        for element in corpus:
            final_prob[element] += damping_factor * 1/len(corpus) 

    return final_prob




def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    random_page = random.choice(list(corpus))
    model = transition_model(corpus, random_page, damping_factor)
    finalprob = {};
    for page in corpus:
        finalprob[page] = 0

    finalprob[random_page] = finalprob[random_page] + 1;


    for i in range(1, n, 1):
        lkey = []
        lp = []
        for element in model:
            lkey.append(element)
            lp.append(model[element])
        random_page = np.random.choice(lkey, 1, p = lp)
        model = transition_model(corpus, random_page[0], damping_factor)
        finalprob[random_page[0]] = finalprob[random_page[0]] + 1;
    
    for page in finalprob:
        finalprob[page] = finalprob[page]/n
        

    return finalprob



def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    final_prob = {}
    for element in corpus:
        final_prob[element] = 1/len(corpus)
    stop = False
    while stop is False:
        count = 0
        for element in corpus:
            probability = (1 - damping_factor)/len(corpus) 
            for element2 in corpus:
                if element in corpus[element2]:
                    probability = probability + damping_factor * final_prob[element2]/len(corpus[element2])
            
            if abs(probability - final_prob[element]) <= 0.001:
                count = count + 1
            final_prob[element] = probability
        
        if count == len(corpus):
            stop = True
    return final_prob
            

if __name__ == "__main__":
    main()
