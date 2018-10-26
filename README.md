# Ph.D. thesis LaTeX files
LaTeX files for producing my Ph.D. thesis in Applied Physics. 

Locations of the official document:
* TBD

#### Title
TBD
#### Author
Roger Ding
#### Date
TBD
#### Advisor(s)
F. Barry Dunning, Thomas C. Killian
#### Degree
Doctor of Philosophy
#### Abstract
TBD
#### Citation
TBD

# Rice University PhD Thesis LaTeX template
The LaTeX PhD thesis template files are located at [PhD Thesis LaTeX template 2008](https://scholarship.rice.edu/handle/1911/21747).
### README.TXT
Package contains template latex files for the PhD thesis at Rice University:

* `thesis_main.tex`: main latex file
* `abstract.tex`: abstract
* `chapter1.tex`: latex file of the thesis chapter (sections, subsections, figures, etc are included in this file)
* `*.bib` files: bibliography files, specified in the main latex file

Necessary style files are also included in the package.


### Note about .gitignore

I couldn't figure out why git wasn't tracking the folder bei1982.OC.42.19/ and bei1982.PS.26.183/ until I stumbled across the solution. 

First, use `git status --ignored` to check which files or folders are being ignored. 

Second, if some files/folders are not tracked, use `git check-ignore --verbose folder_or_file_name` to see what line in the .gitignore is causing them to be ignored.