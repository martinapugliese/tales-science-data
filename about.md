# About this thing

## What's this

This "book" is a personally elaborated collection of material on _Data Science_. The title refers to, without intention to be comparable by any means, Poe's _Tales of Mistery and Imagination_. Traditionally, _science_ has the reputation of something cryptic in the general public, while the enormous rise in _data_ interest these days renders it a grandiose playground for imagination, so I thought the title would capture these two sides of the coin.

Data Science is an interdisciplinary field and a very broad one, somewhat ill-defined, and there is tons of good material in the web; I cannot read it all because I'm only human and my time is limited, there's also countless books I'd like to study, there's countless MOOCs I'd like to take. Because of this, collecting my own notes into a single place helps me a lot in both my learning and in order to have one reference point to go to when in need of info. This is why this project isn't meant to be exhaustive, nor in its best shape: some notebooks are more curated than others depending on the time I spent on them. It is and is meant to be an ongoing project, possible never all clean and finalised.

The other big advantage of doing this is the fact that I keep track of all material explored when dealing with the subject at hand, it is present in the form of references at the bottom of each notebook. It's liek building a taxonomy to navigate the immense archive of knowledge.

Should definitely point out that none of this is a rigorous exposition of the topics. There's way better material on mathematical side of them, and I've always made the effort to list some in the references if you want to dig deeper or read the original sources of an idea.

## How to read this

GitHub renders Jupyter notebooks quite well, but nevertheless does some funny things, for instance with coloured text and internal links. The best, cleanest and most beautiful way to read this is using the Notebook Viewer [**here**](http://nbviewer.jupyter.org/github/martinapugliese/tales-science-data/tree/master/).

## Structure and stylistic choices

After wandering around for a good while, I chose to adopt the [Jupyter notebook](http://jupyter.org) as my mean of communication. Jupyter is, despite looking quite awkward for a collection of mostly written stuff, a brilliant choice. It easily and quickly allows me to do several very important things with no hassle:

1. Write in Markdown format 
2. Embed code in the narration;
3. Embed plots in the narration as well;
4. Write mathematics

For 1., this is super useful when taking a quick note on something with the idea of explanding it later\).

The first versions I was trying to put together of this had been on [GitBook](https://www.gitbook.com/new) or as a good old LateX document. The first proved to be not exhaustive for my needs \(especially for 2. and 3., though being good for 1. and 4.\), the second was just cumbersome for the goal: I'm not writing an academic-like sort of thing.

And because I'm all for sharing and I like the idea of version-controlling the "manuscript", here we go on GitHub.

### How the material is structured

I gave the material the organisation which to me makes more sense, this does not mean that it's the best organisation ever. In fact, some of the topics treated could be potentially categorised differently across folders.

Anyway, each single topic lives in its own notebook, so that it can be read as isolated from all the rest.

Folder names are quite self-explanatory and names of the notebooks have also been kept quite vocal to aid first understanding of what's going to be found inside.

### Style

The CSS and the Matplotlib styles have been customised to suit needs, notebook in [Style demos](https://github.com/martinapugliese/tales-science-data/tree/4f271d78869870acf2b35ce54d40766af7dfa348/Style%20demos.ipnb) illustrates che choices. They are loaded via wrapper methods in each notebook, a procedure mirrored from [this other book](https://github.com/CamDavidsonPilon/Probabilistic-Programming-and-Bayesian-Methods-for-Hackers).

### The references

References are indicated at the end of each notebook, rather than at the global level. This is because I find it much more effective to have a list of further material from within the topic I'm looking at rather than as a separate thing. Furthemore, this allows for a more ordered and structured situation.

When accessible, a link to the PDF in the case of papers is always provided. Otherwise, when paper is not released in open-access and not being made accessible elsewhere by the author\(s\), the link may just point to the journal source.

The file about [beautiful internet](maths/resources.md) contains an updated list of great comprehensive resources on the topics of this book, which are amazing per se and are highly recommended for use and peruse in general.

### The images

Images are of three types:

* I create them in Matplotlib or something \(graphs\)
* I take them from the Internet \(always when reuse is allowed and I give attribution\)
* I draw them by hand, this because to illustrate concepts I find handdrawing to always be the most satisfying and clear mean; they also look nicer than if I did them with a software because I'm not a designer and couldn't do a good job: these ones look typically terrible but I've decided to trade beauty for speed

