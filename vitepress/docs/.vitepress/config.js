import { defineConfig } from 'vitepress'

export default defineConfig({
  title: 'ColonAI Documentation',
  description: 'The Colony That Trades Together',
  lang: 'en-US',
  
  head: [
    ['link', { rel: 'icon', href: '/favicon.ico' }],
  ],
  
  themeConfig: {
    // Logo
    logo: '/logo.svg',
    
    // Navigation
    nav: [
      { text: 'Home', link: '/' },
      { text: 'Documentation', link: '/docs/intro' },
      { text: 'Agents', link: '/docs/agents' },
      { text: 'Architecture', link: '/docs/architecture' },
      { text: 'Getting Started', link: '/docs/getting-started' },
      { 
        text: 'GitHub', 
        link: 'https://github.com/labsmula/ColonAI'
      },
    ],

    // Sidebar
    sidebar: {
      '/docs/': [
        {
          text: 'Getting Started',
          items: [
            { text: 'Introduction', link: '/docs/intro' },
            { text: 'Getting Started', link: '/docs/getting-started' },
          ]
        },
        {
          text: 'Architecture',
          items: [
            { text: 'System Architecture', link: '/docs/architecture' },
          ]
        },
        {
          text: 'Agents',
          items: [
            { text: 'Overview', link: '/docs/agents' },
            { text: 'Scout Agent', link: '/docs/scout-agent' },
            { text: 'Momentum Agent', link: '/docs/momentum-agent' },
            { text: 'Swing Agent', link: '/docs/swing-agent' },
            { text: 'Arb Agent', link: '/docs/arb-agent' },
            { text: 'Yield Agent', link: '/docs/yield-agent' },
            { text: 'Risk Agent', link: '/docs/risk-agent' },
          ]
        },
        {
          text: 'Internal Market',
          items: [
            { text: 'Market Overview', link: '/docs/market-overview' },
            { text: 'Orderbook', link: '/docs/orderbook' },
            { text: 'Lending Pool', link: '/docs/lending-pool' },
          ]
        },
        {
          text: 'Smart Contracts',
          items: [
            { text: 'Contracts Overview', link: '/docs/contracts-overview' },
            { text: 'ColonToken ($COLON)', link: '/docs/colon-token' },
            { text: 'AgentRegistry', link: '/docs/agent-registry' },
            { text: 'Treasury', link: '/docs/treasury' },
            { text: 'ProfitDistributor', link: '/docs/profit-distributor' },
          ]
        },
        {
          text: 'Governance',
          items: [
            { text: 'DAO Overview', link: '/docs/dao-overview' },
            { text: 'Proposal System', link: '/docs/proposal-system' },
            { text: 'Voting', link: '/docs/voting' },
          ]
        },
        {
          text: 'Tokenomics',
          items: [
            { text: 'Tokenomics', link: '/docs/tokenomics' },
            { text: 'Roadmap', link: '/docs/roadmap' },
          ]
        },
        {
          text: 'Reference',
          items: [
            { text: 'API Reference', link: '/docs/api-reference' },
          ]
        },
      ]
    },

    // Footer
    footer: {
      message: 'Copyright © 2024 Mula Labs. Built with VitePress.',
      copyright: 'Copyright © 2024 Mula Labs'
    },

    // Social links
    socialLinks: [
      { icon: 'github', link: 'https://github.com/labsmula/ColonAI' },
    ],
  },
  
  // Build config
  build: {
    sitemap: true,
  },
})
