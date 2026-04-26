# ColonAI - VitePress Documentation

This is a VitePress-based static documentation site for ColonAI.

## 🚀 Features

- ✅ **VitePress** — Modern, fast static site generator
- ✅ **GitBook-like UI** — Clean, professional design
- ✅ **Zero build errors** — Simple, stable
- ✅ **Markdown-native** — Easy to write and maintain
- ✅ **Built-in search** — Instant find docs
- ✅ **Dark mode** — Auto theme switching
- ✅ **Mobile responsive** — Works on all devices

## 📂 Structure

```
vitepress/
├── docs/                  # All markdown files
│   ├── .vitepress/       # VitePress config
│   │   └── config.js
│   ├── index.md            # Landing page
│   ├── intro.md           # Introduction
│   ├── getting-started.md   # Setup guide
│   ├── architecture.md       # System architecture
│   └── ... (all other docs)
├── package.json            # Dependencies & scripts
└── README.md              # This file
```

## 🛠️ Development

```bash
# Install dependencies
npm install

# Start development server
npm run docs:dev

# Build for production
npm run docs:build

# Preview production build
npm run docs:preview
```

## 🚀 Deployment

### Vercel (Recommended)

1. **Setup Vercel:**
   - Install Vercel CLI: `npm i -g vercel`
   - Login: `vercel login`

2. **Deploy:**
   ```bash
   cd vitepress
   vercel --prod
   ```

3. **Output:**
   - URL: `https://colonai-docs.vercel.app`
   - Auto-rebuild on push

### GitHub Pages

```bash
# Build
npm run docs:build

# Push to gh-pages
git subtree push --prefix vitepress origin gh-pages
```

### Netlify

```bash
# Build
npm run docs:build

# Netlify will auto-deploy
# Just connect Git repository
```

## ✅ Status

- ✅ All docs migrated from docs-ui/
- ✅ VitePress config ready
- ✅ Navigation & sidebar setup
- ✅ Mobile responsive & dark mode
- ✅ Built-in search enabled

## 📚 Documentation

Complete docs available at:
- **Source:** `/docs` folder
- **Preview:** `npm run docs:dev`
- **Deploy:** Vercel/GitHub Pages/Netlify

---

Built with ❤️ by Mula Labs using [VitePress](https://vitepress.dev/)
