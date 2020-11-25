# Reference: https://jaketae.github.io/blog/jupyter-automation/
#!/usr/bin/python
import sys, re

def edit():
	path = "/home/anilg/projects/newblog/docs/_jupyter/" + str(sys.argv[1])
	yaml = "---\ntitle: TITLE\nexcerpt: Shortexcerpt\nheader:\n  - overlay_image: HEADERIMAGE\n  - overlay_filter: 0.5\n  - caption: CAPTION\nnbviewer: bitlylink\nmathjax: true\ntags:\n  - tag\n---\n\n"
	with open(path, 'r') as file:
		filedata = file.read()
	filedata = re.sub(r"!\[png\]\(", "<img src=\"/assets/images/", filedata)
	filedata = re.sub(".png\)", ".png\">", filedata)
	filedata = yaml + filedata
	with open(path, 'w') as file:
		file.write(filedata)

if __name__ == '__main__':
	edit()
