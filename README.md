# bygeorge
A personal static site using [Pelican](http://docs.getpelican.com/en/3.6.3/index.html).

# How To ...

**A word of caution for CodeKit users**: CodeKit will generate HTML output from Markdown (so does Pelican), duplicating the efforts typically into the wrong directory. Turn this off to avoid utter madness.

### Set up virtualenv and install Pelican

(Just do this. Small headache now is better than chronic migraine later.)

1. pip install virtualenv (Google it.)
2. Create a folder called `virtualenvs` wherever you keep your projects.
3. In command line type: `virtualenv [wherever-your-virtualenvs-dir-is]/pelican`
4. Change to that newly created pelican directory.
5. Type: `source bin/activate` (You should see `(pelican)` appear at the beginning of your command prompt.)
6. Type: `pip install pelican markdown typogrify`
7. Type: `pelican-quickstart` and follow the instructions. Be sure to specify a directory where you want your site to live otherwise all your site files will be dumped into your virtualenv root. (More info [here](http://docs.getpelican.com/en/3.6.3/install.html).)

### Work with a remote GitHub repository and a second computer

1. Upload whatever directory you chose to build your site in (Step 7 above) to a fresh repository.
2. On your second machine follow steps 1 through 6.
3. Change to your `pelican` directory and clone the repository: `git clone [link-to-your-repository]`.
4. Carry on with development and push changes back to the remote on GitHub. 

# To Do ...

* Style changes
	* Image handling
	* Explore menu options
		* Idea: Fixed footer w/ 3 button nav.
* IFTTT integrations
	* Take a photo >> post to blog
	* Tag an Evernote >> post to somewhere
* CV/résumé
* Look into [Piwik analytics](https://piwik.org/)
* Explore [plugins](https://github.com/getpelican/pelican-plugins)
