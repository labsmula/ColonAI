# ColonAI Documentation UI

This is the Docusaurus-based documentation platform for ColonAI.

## Quick Start

```bash
# Install dependencies
npm install

# Start development server
npm start

# Build for production
npm run build

# Serve production build
npm run serve
```

## Project Structure

```
docs-ui/
├── docs/                  # Documentation markdown files
│   ├── intro.md
│   ├── getting-started.md
│   ├── architecture.md
│   └── ...
├── src/                   # Custom styles and components
│   ├── css/
│   │   └── custom.css
│   └── pages/
├── static/               # Static assets (images, etc.)
├── blog/                 # Blog posts
├── sidebars.js           # Sidebar configuration
├── docusaurus.config.js   # Docusaurus configuration
└── package.json          # Node.js dependencies
```

## Deployment

### GitHub Pages

```bash
npm run deploy
```

### Vercel

```bash
npm run build
vercel --prod
```

## Customization

- **Theme:** Modified default Docusaurus theme
- **Colors:** Custom primary colors (green for ColonAI branding)
- **Plugins:** None configured yet

## Resources

- [Docusaurus Docs](https://docusaurus.io/docs)
- [MDX Syntax](https://mdxjs.com/docs/what-is-mdx/)
- [React](https://react.dev)

---

Built with ❤️ by Mula Labs
