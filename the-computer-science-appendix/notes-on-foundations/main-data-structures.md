# \(Main\) data structures

A data structure is a higher level form based on top of primitive data types \(integers, floats/doubles, characters, booleans\). Let's quickly go through the main ones.

## Arrays

Lists \(collections\) of elements. Note that Python has the concept of array and that of list: they differ both in their nature and what you can do with them and their general purpose. See the article in the [references](main-data-structures.md#references) for a nice comparison.

## Linked lists

This is a list of elements \(called _nodes_\) linked one to the next: a node contains the element and the link to the next node. This structure allows for easy replacement, insertion and deletion of elements as they are not stored in contiguous places in the memory, thanks to the links.

## Hash tables

Hash tables are key - value pairs, they are super useful: you can access a value by calling its key so the lookup is straightforward \(in O\(1\) time\). Hash tables use a hash function to map the key \(which can be of any type\) to a numerical value, so that given a key the computer knows where is the value to be accessed and can do in constant time \(without the need to scroll\).

Dictionaries in Python are hash tables - have a read at the blog in the [references](main-data-structures.md#references) about this.

## Stacks and queues

A stack is a data structure where you put elements in one on top of the other and it uses the LIFO philosophy to get data out: "last in first out" means that you access elements in the reverse order than the one used to put them in.

A queue is similar, but uses the FIFO philosophy: "first in first out", basically elements come out from the other end than the one you've inserted them in.

## Graphs

Graphs have nodes and connections between them which determine their relation. There is a whole branch of mathematics devoted to their study \(graph theory\). A tree is a special type of graph where there is a clear relation between a parent node and a child node, so no cycles appear \(there are hierarchical relations\).

There are several subtypes of graphs, identified by their main characteristics.

## Objects

An object is a collection of data and, sometimes, functions that work on this data, put together in a coherent place. Normally, an object is implemented via a class. 

For example, a `AlarmClock` object will represent the alarm clock you have on your bedside table: it will store data for the date and time and will have methods to update the time as it goes and ring based on some criteria \(always at the same time daily or with better sophistication\).

You can use them to build objects that inherit characteristics from others and specialise. For instance, you can do a general class for `Vehicle` and one for a `Train` that inherits from it as it is a subclass of it \(the basic features will be inherited and specific ones are implemented for it only\).

The Python docs for classes is quite educational!

## References

1. _Gayle Laakmann McDowell_, **Cracking the Coding Interview**, CareerCup
2. _Kateryna Koidan_, ****[**Array vs. List in Python – What's the Difference?**,](https://learnpython.com/blog/python-array-vs-list/) an article on LearnPython.com
3. Aaron Meurer's blog, [**What happens when you mess with hashing in Python**](https://www.asmeurer.com/blog/posts/what-happens-when-you-mess-with-hashing-in-python/)\*\*\*\*
4. [Classes in Python](https://docs.python.org/3/tutorial/classes.html), from the docs

