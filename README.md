# anilgeorge.space

Personal notes. Built with Jekyll and published by GitHub Pages from `main`.

## Write a note (directly on github.com)

1. Open the `_posts` folder and create a new file
2. Name it `YYYY-MM-DD-short-name.md`, for example `2026-11-02-a-slow-morning.md`.
   The `short-name` becomes the address: `anilgeorge.space/notes/a-slow-morning/`.
3. Paste this at the top, then write below it in Markdown:

   ```markdown
   ---
   title: A slow morning
   date: 2026-11-02
   ---

   Start writing here.
   ```

4. **Commit changes** to `main`. The note is live in a minute or two.

The same template lives in `_templates/note.md`.

## Write a note (on your computer)

```bash
bundle install          # first time only
bundle exec jekyll serve
```

Preview at http://localhost:4000. Add new note to `_posts/` as above, then commit and push to `main`.

## Markdown cheatsheet

`## Heading`, `*italic*`, `**bold**`, `[link](https://…)`, `> quote`, `- list`, `` `code` ``, and `---` for a small three-dot break. For a poem or long quote, keep line breaks with `<p class="verse">line one<br>line two</p>`. Images go in `assets/images/` and are added with `![description](/assets/images/file.jpg)`.

## Good to know

- This repository is public, so anything committed here, including drafts, can be read by anyone.
- To change a published note, edit its file. To remove one, delete its file.
- Keep the `CNAME` file. It holds the custom domain.
- Fonts: Newsreader, under the SIL Open Font License (`assets/fonts/OFL.txt`).
