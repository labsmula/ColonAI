/**
 * Creating a sidebar enables you to:
 - create an ordered group of docs
 - render a sidebar for each doc of that group
 - provide ordering/visibility control for sidebar doc items

 You can choose not to use a sidebar at all if you don't want the sidebar feature.
 */

const sidebars = {
  // By default, Docusaurus generates a sidebar from the docs folder structure
  tutorialSidebar: [
    'intro',
    'getting-started',
    'architecture',
    'agents',
    {
      type: 'category',
      label: 'Agents',
      items: ['scout-agent', 'momentum-agent', 'swing-agent', 'arb-agent', 'yield-agent', 'risk-agent'],
    },
    {
      type: 'category',
      label: 'Internal Market',
      items: ['market-overview', 'orderbook', 'lending-pool'],
    },
    {
      type: 'category',
      label: 'Smart Contracts',
      items: ['contracts-overview', 'colon-token', 'agent-registry', 'treasury', 'profit-distributor'],
    },
    {
      type: 'category',
      label: 'Governance',
      items: ['dao-overview', 'proposal-system', 'voting'],
    },
    'tokenomics',
    'roadmap',
    'api-reference',
  ],
};

export default sidebars;
