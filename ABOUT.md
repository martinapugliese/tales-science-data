# About this book

## What's this

This book is a personally elaborated collection of material on _Data Science_. 

The title refers to, without intention to be comparable by any means, Poe's _Tales of Mistery and Imagination_. Traditionally, _science_ has the reputation of something cryptic in the general public, while the enormous rise in data talk these days renders data itself a grandiose playground for imagination.

Data Science is an interdisciplinary field and a very broad one, somewhat ill-defined, and there is literally loads of good material in the web. Many of it I cannot read because (it's an old problem) I'm only human and my time is limited. There's also countless books I'd like to study, there's tons of MOOCs I'd like to take. 

Truth is, I desired a platform where to order my personal elaboration of the material which, one way or the other, relates to Data Science, and to keep it clean. When I was at Uni pen and paper was great for the job but now there's much more "interactivity" involved into this, and also, I want a way to be able to go back to things, add new stuff, modify it.

Said material is a put-together of things I learned ages ago (at Uni), of things I learned more recently, of things I learn in my everyday job. I try, whenever possible to understand things from principles and dissect them into their components, that's what really interests me. 

This is my personally worked presentation. I also take advantage, by writing all this, to keep track of all the great references which helped and still help me learn more in the area. 

## How to read this

GitHub renders Jupyter notebooks quite well, but nevertheless does some funny things, for instance with coloured text and internal links. The best, cleanest and most beautiful way to read this is using the Notebook Viewer [**here**](http://nbviewer.jupyter.org/github/martinapugliese/tales-science-data/tree/master/).

## Structure and choices

After wandering around for a good while, I chose to adopt the [Jupyter notebook](http://jupyter.org) as my mean of communication. 

Jupyter is, despite looking quite awkward for a collection of rather theoretical materials, a brilliant choice. It easily and quickly allows me to do several very important things with no hassle:

1. Write in Markdown format 
2. Embed code in the narration;
3. Embed plots in the narration as well;
4. Write mathematics

For 1., this is super useful when taking a quick note on something with the idea of explanding it later).

The first versions I was trying to put together of this had been on [GitBook](https://www.gitbook.com/new) or as a good old LateX document. The first proved to be not exhaustive for my needs (especially for 2. and 3., though being good for 1. and 4.), the second was just cumbersome for the goal: I'm not writing an academic-like sort of thing.

And because I'm all for sharing and I like the idea of version-controlling the manuscript, here we go on GitHub. 

### How the material is structured

I gave the material the organisation which to me makes more sense, this does not mean that it's the best organisation ever. In fact, some of the topics treated could be potentially categorised differently across folders.

Anyway, each single topic lives in its own notebook, so that it can be read as isolated from all the rest. 

Folder names are quite self-explanatory and names of the notebooks have also been kept quite vocal to aid first understanding of what's going to be found inside. 

### Style

The CSS and the Matplotlib styles have been customised to suit needs, notebook in [Style demos](Style demos.ipnb) illustrates che choices. 
They are loaded via wrapper methods in each notebook, a procedure mirrored from [this other book](https://github.com/CamDavidsonPilon/Probabilistic-Programming-and-Bayesian-Methods-for-Hackers).

### The references

References are indicated at the end of each notebook, rather than at the global level. This is because I find it much more effective to have a list of further material from within the topic I'm looking at rather than as a separate thing. Furthemore, this allows for a more ordered and structured situation.