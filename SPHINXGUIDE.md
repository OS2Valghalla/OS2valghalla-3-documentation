# Quick-start Sphinx and reStructuredText guide
This guide will help you get started with Sphinx and write documentation in reStructuredText markup.

Work in progress, more content to be added.

This quick-guide will cover:
1. [General syntax and formatting](#1-general-syntax-and-formatting)
2. [Common elements](#2-common-elements)
3. [How to create and structure documentation pages](#3-how-to-create-and-structure-documentation-pages)
4. [Basic templating and theming](#4-basic-templating-and-theming)
5. [Recommended extensions](#5-recommended-extensions)

## 1. General syntax and formatting
This section describes commonly used syntax and formatting.
### Standard inline markup
* *Italic* text: Use one asterisks to create bold text, for example ``*text*``
* **Bold** text: Use two asterisks to create bold text, for example `**text**`
* Inline code: Use backquotes to create inline code, for instance ` ``text`` `. This converts the text to monospace font, adds a background, and changes the text color. This should only be used for simple code examples. For more advanced or multiline code use code blocks.

### Comments
Comments can be added in the markup, which does not display on the page itself. To create a comment prefix the comment text with `..`.

**Example**
```
.. This is a comment.
```

To create a multiline comments, add a linebreak between the `..` prefix and the comment text, and indent each line with two whitespaces.

**Example**
```
.. 
  This is a multiline comment.
  This is another line in the same comment.
```

### Hyperlinks
There are two kinds of hyperlinks, external and internal.
#### **External hyperlinks**
Standard hyperlinks needs to be wrapped in backquotes and suffixed with an underscore. 

**Example:**
```
`This is a link to Google <https://google.com/>`_
```

The link text and target can also be separated, which is useful if the same link is used several times.

**Example:**

Link text:
```
This is a link to `Google`_
```

Target:
```
.. _Google: https://google.com/
```
The target needs to be place at the end of the section and be suffixed with `.._`.

#### **Internal hyperlinks and cross-references**
Internal hyperlinks are great for creating references to other pages or sections in the documentation. The element being referred to needs to have a reference label. 

**For example:**
```
.. _dependencies-angular:

Angular dependencies
------------------------------
```
The section can then be referred to by using the built-in :ref: role. 

**For example:**
```
See the section :ref:`dependencies-angular` to read more about Angular dependencies.
```

#### **Glossary of terms**
The project comes with a pre-created glossary file. 

Terms can be added to this glossary, which can then be used with the :ref: role.

For example, to make a reference to a term in the glossary called “Angular”:
```
The framework :ref:`Angular` is used for this project.
```

### Sections and headers
Sphinx pages support multiple levels of headings. Headings and sections are very important for the documentation, as they are automatically added to the navigation and table of contents, furthermore they can be referenced to from other pages in the documentation.

Usually no more than 3 levels of headings are needed; title, subsection, and subsubsection.

* **Titles** are underlined with ``=``
* **Sections** are underlined with ``-``
* **Subsection** are underlined with ``~``

**Note:** It is important that the underlines are at least the same width as the header text, for example:
```
This title is underlined correctly
==================================
```
```
This title is NOT underlined correctly
===========
```
Headers can be referenced using the ``:ref:`` role, as described in the [Hyperlinks](#hyperlinks) section.


## 2. Common elements
There are several body elements supported by Sphinx out-of-the-box.

### Table of content
Automatic generation of table of contents is one of the strongest features of Sphinx.

To create a table of contents, the `.. toctree::` directive can be used. Pages can be added to the ToC by either referencing the name of the RST file itself, or use the title of the page.

**Example**
```
.. toctree::

   user-interface-design
   user-interface-guidelines
```

The `.. toctree::` directive supports several options, such as numbering, max depth, and automatic inclusion of sub-pages. See the offical [Sphinx documentation of table of contents](https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html#table-of-contents) to read all possible options.

**Example of a ToC using max-depth and automatic numbering**
```
.. toctree::
   :maxdepth: 2
   :numbered:

   user-interface-design/index
   user-interface-guidelines/index
```

### Lists
Bullet point lists needs to be prefixed with `*`
```
* Bullet point 1
* Bullet point 2
```
Numbered lists needs to be prefixed with a number and a period
```
1. List item 1
2. List item 2
```
Numbered lists can also be autonumbered using `#`
```
#. List item 1
#. List item 2
```
Nested lists can be created by add a line-break after the parent list item and indenting the nested list item with two spaces:
```
* List item 1
* List item 2

  * Nested item 1
  * Nested item 2

*  List item 3
```

### Notes and warnings
Notes and warnings are great for highlighting important information for the reader.
A note can be created using the `.. note::` directive. A linebreak needs to be added after the note directive with the note text added underneath. The note text needs to be indented with two whitespaces.
Example
```
.. note:: 
   This is a note.
   Multilines are supported.
```
#### Note types
Several types of notes are supported, such as warnings and hints. The `.. note` part of the directive just have to be replaced with the name of the note type to be used.
**Example of a warning note**
```
.. warning:: 
   This is a warning note.
```
These are the supported note types:
* note
* warning
* attention
* caution
* danger
* error
* hint
* important
* tip

### Line blocks
Line blocks are used to create a block of indented text.

To create a line block, the text should be prefixed with `::` and be followed by a linebreak before the line block text. The line block text itself has to be indented by two whitespaces.

**Example**

```
This is a line block::
  This is the text in the block

  Multiline text is supported
```

### Code blocks
Code blocks are the standard way to create a block of code with code highlight.

The code block can be created using the `.. code-block::` directive. To specificy a specific code language for highlighting, the directive should be followed by the name of the language.

**Example of a code block with a standard Python loop**
```
.. code-block:: python

   fruits = ["apple", "banana", "cherry"]
   for x in fruits:
   print(x)
```

### Tables
Sphinx support tables, with several options such as automatic with, alignments, grids, and CSV tables. See the [official documentation of the Sphinx Table directive](https://docutils.sourceforge.io/docs/ref/rst/directives.html#table) to read more.

:warning: Since Sphinx is based on Python, every whitespace is important in the markup. It is recommended to use an extension to help formatting tables, such as the [Table Formatter](https://marketplace.visualstudio.com/items?itemName=shuworks.vscode-table-formatter) VS Code extension, mentioned in the [Recommended extensions](#5-recommended-extensions) section.

**Example of a table with headers, two columns and three rows**
```
.. table:: 

   ======  ======
   Fruit   Amount
   ======  ======
   Banana  9
   Apple   12
   Cherry  5
   ======  ======
```

The table directive also supports grid format

**Example of grid table**
```
.. table:: 

   +--------+--------+
   | Fruit  | Amount |
   +========+========+
   | Banana | 9      |
   +--------+--------+
   | Apple  | 12     |
   +--------+--------+
   | Cherry | 5      |
   +--------+--------+
```

### Images
Images can be inserted in the content using the ``.. image`` directive.

Example of external image:
```
.. image:: https://www.domain.com/image1.png
```
Example of internal image:
```
.. image:: image1.png
```
By default links to internal images have to be placed in the same folder as the RST page.
It is good practice to use subfolders for media, to keep images and figures separate from RST pages. 

To insert an image placed in a subfolder, the folder name needs to be suffixed.

For example, if the subfolder is called media:
```
.. image:: media/image1.png
```

### Figures
Figures act much like images, but makes it possible to add a caption to the image and an optional legend.

Example of inserting a figure with a caption:
```
.. figure:: image1.png

   This is the caption of the figure.
```
**Note:** it is important that there is a line-break between the image and the caption, and that there is a space before the caption.

# 3. How to create and structure documentation pages
This section will cover how to create new documentation pages, and how to structure them to create to correct hierarchy.

Pages are created in the [docs/source](docs/source) folder.

It is important to use the correct structure to create the correct hierarchy of pages and sub-pages. This hierarchy will automatically be used for the sidebar navigation and the [table of content](#table-of-content).

This project supports pages up to a maximum depth of 3, excluding the frontpage.
For example, to create a "User Interface Design" page, with "Administration" and "External Web" sub-pages, where each of them have their own "Dependencies" sub-page, the structure would be the following:
```
1. User Interface Design
  1.1 Administration
    1.1.1 Dependencies
  1.2 External Web
    1.2.1 Dependencies
2. User Interface Guidelines
```

To create a sub-page, create a new sub-folder and a new RST in the folder. For instance, to create a the "Administration" sub-page and the "dependencies" sub-page shown above, use the following folder structure:

```
Administration page:
user-interface-design/administration/index.rst
Dependencies sub-page:
user-interface-design/administration/dependencies/dependencies.rst
```

The filename `index.rst` is often used for the sub-page that includes the table of contents of the sub-pages.

All RST pages needs to use the `.rst` filetype.

# 4. Basic templating and theming
This section will cover how to create new HTML templates and how to style them.

# 5. Recommended extensions
This section gives an overview of optional extensions, which can be used to improve the experience when editing documentation pages.
## Live Preview
The following extensions can be used to setup a live preview for editing. A live preview shows the output HTML files in real time while editing.

### Esbonio (VS Studio Code extension)
The VS Studio Code extension ["Esbonio"](https://marketplace.visualstudio.com/items?itemName=swyddfa.esbonio) can provide live-preview, syntax highlight, and auto-completion for reStructeredText.

> :warning: Be sure the right Python interpreter is selected before starting the Esbonio server. See the [*Build project*](INSTALLATION.md#3-build-the-project) section of the [Quick-start installation guide](INSTALLATION.md#3-build-the-project).

### reStructuredText (VS Studio Code extension)
The VS Studio Code extension ["reStructuredText"](https://marketplace.visualstudio.com/items?itemName=lextudio.restructuredtext&ssr=false#overview) is the a live-preview extension officialle recommended by Read the Docs. Just like the ["Esbonio"](https://marketplace.visualstudio.com/items?itemName=swyddfa.esbonio) extension it provides live-preview, syntax highlight, and auto-completion for reStructeredText.

This extension provides almost the same features as the [Esbonio](#esbonio-vs-studio-code-extension) extension, but is more complex to setup. Therefore [Esbonio](https://marketplace.visualstudio.com/items?itemName=swyddfa.esbonio) is recommended if none of the advanced features are needed.

> :warning: Be sure the right Python interpreter is selected before enabling the preview feature. See the [*Build project*](INSTALLATION.md#3-build-the-project) section of the [Quick-start installation guide](INSTALLATION.md#3-build-the-project).

### Sphinx Autobuild
[Sphinx Autobuild](https://sphinx-extensions.readthedocs.io/en/latest/sphinx-autobuild.html) is a Python extension, which means it does not require a specific code editor. The extension is not technically a live-preview, as it re-builds HTML pages on save. The HTML pages are served locally and can be accessed directly in the browser, giving an exact preview of how the HTML pages will look when hosted online, such as on Read the Docs.

To setup the extension for this project, run the following command in the environment:
```
pip install sphinx-autobuild
```
Then run the following to enable re-building on save:
```
sphinx-autobuild docs/source docs/source/_build/html
```
By default the HTML files can be accessed in the browser at ```http://127.0.0.1:8000/```.

## Syntax and formatting
The following extensions can help improve the experience of syntax and formatting.

### reStructuredText Syntax highlighting (VS Code extension)
The ["reStructuredText Syntax highlight"](https://marketplace.visualstudio.com/items?itemName=trond-snekvik.simple-rst&ssr=false#review-details) extension for VS Code makes it easier to differentiate text and components in the markiå.

A syntax highlight extension is highly recommended, as reStructuredText is fairly complex and hard to work with without any syntax highlighting. Visual Studio Code does not have out-of-the-box syntax highlight support for reStructuredText.

**Note** that both the [Esbonio](#esbonio-vs-studio-code-extension) and the official [reStructedText](#restructuredtext-vs-studio-code-extension) extensions comes with their own syntax highlighter.

### Table Formatter (VS Code extension)
Creating and formatting tables in RST can be very complex, as correct use of whitespaces can make or break tables. Therefore the [Table Formatter](https://marketplace.visualstudio.com/items?itemName=shuworks.vscode-table-formatter) extension is recommended to help create correctly formatted tables.