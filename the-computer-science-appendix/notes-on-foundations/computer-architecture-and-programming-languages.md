# Computer architecture and programming languages

## Computer architecture - just some notes

We'll outline some stuff about computers here, a lot of it being prompted by reading Plantz's [book](computer-architecture-and-programming-languages.md#references) and then digging around.

### Bits, representations and bytes

_Bit_ stands for binary digit and it's a switch representation: you got a switch which can take a binary value. 8 bits compose the so called _byte_, and this is a convention which grew to be agreed upon with time: changing with hardware and operating system. IBM in 1956 established the 8-bit standard, which won over other systems because it could accommodate the 256 [ASCII](http://ee.hawaii.edu/~tep/EE160/Book/chap4/subsection2.1.1.1.html) characters: 26 upper chars, 26 lower chars, the 10 digits and the most important punctuation marks. Because with time we need to represent more things though, the choice of only 255 was not enough anymore and so architectures with more than one by came to be \(see the [Quora page](computer-architecture-and-programming-languages.md#references)\).

#### Note on the hexadecimal system

In computers, the binary and hexadecimal \(base 16\) systems for number representation are used.

In base 16, you have

* 0 is$$0_{10}$$ 
* 1 is$$1_{10}$$ 
* 9 is$$9_{10}$$ 
* a is$$10_{10}$$ 
* b is$$11_{10}$$ 
* ...
* 10 is$$16_{10}$$ 
* ...

Numbers prefixed with 0x in C/C++ means they are expressed in base 16.

### RAM

The phrasing _random access_ is rather misleading. It's not a random memory in the sense that stuff is placed in random spots, _random access_ means it uses the same time to access each byte in memory, as opposed to a tape which you'd have to walk for access at a specific location. More specifically, it means that a program accesses variables which have been allocated in some places of the memory and does not look for them by scrolling sequentially.

## A short and very non-comprehensive timeline of languages

* 1949 Assembly: low-level, strong correspondence to machine code
* 1957 Fortran
* 1978 C, low-medium level
* 1983 C++
* 1991 Python
* 1995 Java

About Fortran, and why it still is so common within the scientific programming circles, have a read at this brilliant article on [Ars Technica](computer-architecture-and-programming-languages.md#references).

### Main programming paradigms

A programming paradigm is a style of coding. The main ones are

* imperative 
* declarative \(of which functional is a subset\)
* object-oriented

#### Imperative and declarative

Are two opposing ones. In an _imperative_ paradigm, algorithms are implemented in explicit steps and statements are used to change the state: statements are the smallest standalone instructions. In a _declarative_ paradigm, algorithms are logically expressed without the explicit list of instructions \(for example with the use of list comprehensions in Python\).

#### Object oriented

In an _object-oriented_ programming paradigm, objects are declared that contain attributes and methods.

#### Functional

The _functional_ programming paradigm, belonging to the declarative class, treats computation as the evaluation of mathematical functions and is based on lambda calculus, avoiding statements. Examples of functional languages are Clojure, Haskell; other that support the functional paradigm are Python, R, Java, Scala.

For example, in Clojure you'd get the square of integers until 25 as

```text
(take 25 (squares-of (integers)))
```

where `take`, `squares-of` and `integers` are functions, as opposed to an explicit for loop you'd write in other languages.

Scala is a functional programming language that runs on the JVM \(Java virtual machine\), meaning it gets compiled to Java bytecode, it is statically typed, object-oriented. The name stands for "scalable language" because it has been conceived to grow with demand of its users. The project started in 2001 at the E. Polytechnique de Lausanne by M Odersky and it is taking more and more interest in the data science community.

### Compiled and interpreted languages

A _compiler_ is something, like a parser, that transforms the source code the programmers uses into machine code \(binary file with low-level instructions the machine understands\). Compiled languages are for instance C, C++, Fortran.

An _interpreter_ interprets the language, in that when you write your high-level instructions it goes searching for the corresponding binary code, which is part of itself. The difference with a compiler is that this process is executed at run time, making interpreted code sensibly slower than compiled one. Examples are Python and Ruby.

### Statically and dynamically typed languages

In a statically typed language, you cannot change the type of a variable after you've declared it. Python is a dynamically typed one as you can do things like

```python
a = 1

...

a = "bla"
```

## References

1.  R G Plantz, **An Introduction to Computer Organisation**, 2015
2.  [Quora on why are there 8 bits in a byte](https://www.quora.com/Why-it-is-that-1-Byte-is-equal-to-8-Bits)
3.  [Scientific computing’s future: Can any coding language top a 1950s behemoth?](https://arstechnica.com/science/2014/05/scientific-computings-future-can-any-coding-language-top-a-1950s-behemoth/), an article about Fortran still being used today in numerical work, _Ars Technica_, 2014

