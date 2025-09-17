# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Jekyll-based personal blog using the Minimal Mistakes theme. The site is built with Jekyll, uses Ruby gems for dependencies, and includes JavaScript build processes for asset optimization.

## Architecture

- **Jekyll Static Site Generator**: Uses Minimal Mistakes theme (v4.21.0) via remote_theme
- **Content Structure**: 
  - `_posts/` directories organized by category (`musings/`, `opinions/`, `workbench/`)
  - `_pages/` for static pages (about, 404, categories, etc.)
  - `_includes/`, `_layouts/`, `_sass/` for theme components
- **Asset Management**: JavaScript files are concatenated and minified via npm scripts
- **Deployment**: GitHub Pages compatible with Travis CI configuration

## Development Commands

### Building and Serving
```bash
# Install Ruby dependencies
bundle install

# Install Node dependencies  
npm install

# Build the site locally
bundle exec jekyll build

# Serve locally with auto-reload (default Jekyll command)
bundle exec jekyll serve

# Advanced preview with custom auto-regeneration
bundle exec rake preview
```

### Asset Processing
```bash
# Build optimized JavaScript assets
npm run build:js

# Watch JavaScript files for changes
npm run watch:js

# Minify JavaScript files
npm run uglify

# Add banner to minified files
npm run add-banner
```

## Content Guidelines

### Posts
- Posts are organized in category-specific `_posts/` directories
- Categories: `musings`, `opinions`, `workbench`
- Follow Jekyll naming convention: `YYYY-MM-DD-title.md`
- Front matter should include appropriate category and tags

### Pages
- Static pages go in `_pages/` directory
- Use appropriate layout (typically `single`)
- Set `author_profile: false` unless needed

## Configuration

### Main Config
- Site configuration in `_config.yml`
- Theme: Minimal Mistakes with "contrast" skin
- Analytics: Google Analytics enabled
- Social links: Twitter, LinkedIn, GitHub configured

### Build Process
- Jekyll excludes development files (node_modules, package.json, etc.)
- Sass compilation configured with compressed output
- HTML compression enabled for production

## Key Files

- `_config.yml`: Main Jekyll configuration
- `package.json`: Node.js dependencies and build scripts  
- `Gemfile`: Ruby gem dependencies
- `Rakefile`: Custom rake tasks including preview functionality
- `banner.js`: Script to add banners to built assets