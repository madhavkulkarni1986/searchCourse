##### Inspired by Medium post 
##### => Post  : Build a Searchable Course Catalog => https://stories.mlh.io/build-a-searchable-course-catalog-8a0553824af5
##### => Author: Irfaan Khalid(https://stories.mlh.io/@Irfdawg).

###### The original post shows the implementation using Node.js and some additional libraries. Here I am use Python; request and BeautifulSoup modules :-)


#### Examples

``` 
>>> import getCourse
>>> getCourse.search('Data')
COURSE => 01:198:112
                 TITLE => Data Structures (4)
                 DESCRIPTION =>   Queues, stacks, trees, lists, and recursion; sorting   and searching; hashing; complexity of algorithms; graph   representations and algorithms.
                 PREREQUISITE => Prerequisites: 01:198:111 and CALC1. Credit not given for both this course and 14:332:351.


COURSE => 01:198:142
                 TITLE => Data 101 (3)
                 DESCRIPTION => Topics in data literacy for nonmajors in computer science or statistics.
                 PREREQUISITE => Prerequisite: 01:640:025 or placement. Credit not given for both this course and 01:960:142.


COURSE => 01:198:336
                 TITLE => Principles of Information and Data Management (4)
                 DESCRIPTION =>   Describing and querying various forms of information   such as structured data in relational databases, unstructured text (IR),   semistructured data (XML, Web), and deductive knowledge. Conceptual   modeling and schema design. Basics of database management systems services   (transactions, reliability, security, and optimization). Advanced topics:   finding patterns in data, information mapping, and integration.
                 PREREQUISITE => Prerequisites: 01:198:112; 01:198:205 or 14:332:312.


COURSE => 01:198:437
                 TITLE => Database Systems Implementation (4)
                 DESCRIPTION => Focuses on the
implementation of database management systems (DBMS). Provides students the tools to
understand the internals of a DBMS: transaction management, query processing
and query optimization, implementation of systems handling text data,
and management issues in a web context.
                 PREREQUISITE => Prerequisites: 01:198:214 and 336.


COURSE => 01:198:439
                 TITLE => Introduction to Data Science (4)
                 DESCRIPTION => Focuses on algorithms and tools for solving data-science problems, including preparation, characterization and presentation, analysis, and applications.
                 PREREQUISITE => Prerequisites: 01:198:206, 336.


>>>
```

#### From command line
```
$ python getCourse.py
Usage: python getCourse.py '<search term>'
Error: Invalid number of parameters. You forgot to mention the search term

$ python getCourse.py 01:198:336
COURSE => 01:198:336
                 TITLE => Principles of Information and Data Management (4)
                 DESCRIPTION =>   Describing and querying various forms of information   such as structured data in relational databases, unstructured text (IR),   semistructured data (XML, Web), and deductive knowledge. Conceptual   modeling and schema design. Basics of database management systems services   (transactions, reliability, security, and optimization). Advanced topics:   finding patterns in data, information mapping, and integration.
                 PREREQUISITE => Prerequisites: 01:198:112; 01:198:205 or 14:332:312.


$
```
