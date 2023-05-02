# Quick-start Sphinx and reStructuredText guide
This guide will help you get started with Sphinx and write documentation in reStructuredText markup.

Work in progress, more content to be added.
# Sphinx
This section will cover:
1. How to create and structure documentation pages
2. Basic templating and theming
3. How to build the project

# reStructuredText
This section will cover:
1. General syntax of RST markdown
2. Common components
3. How to create and structure documentation pages
4. How to use directives
5. How to use roles

# Extensions
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
The ["reStructuredText Syntax highlight"](https://marketplace.visualstudio.com/items?itemName=trond-snekvik.simple-rst&ssr=false#review-details) extension for VS Code makes it easier to differentiate text and components in the markdown.

A syntax highlight extension is highly recommended, as reStructuredText is fairly complex and hard to work with without any syntax highlighting. Visual Studio Code does not have out-of-the-box syntax highlight support for reStructuredText.

**Note** that both the [Esbonio](#esbonio-vs-studio-code-extension) and the official [reStructedText](#restructuredtext-vs-studio-code-extension) extensions comes with their own syntax highlighter.