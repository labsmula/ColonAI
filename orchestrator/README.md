# ColonAI Orchestrator

Backend orchestrator for ColonAI multi-agent trading system.

## Project Structure

```
orchestrator/
├── src/
│   ├── agents/              # Base agent class & implementations
│   ├── market/             # Market engine (internal market, mock DEX, price feed)
│   ├── risk/               # Risk engine & position manager
│   ├── communication/       # Event bus & agent messaging
│   ├── chain/               # Smart contract interaction
│   ├── storage/             # 0G Storage integration
│   └── config.ts          # Configuration
├── index.js               # Entry point
├── package.json
└── .env.example
```

## Installation

```bash
npm install
```

## Development

```bash
npm run dev
```

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| /agents | GET | List all registered agents |
| /agents/:id | GET | Get agent details |
| /agents/:id/start | POST | Start an agent |
| /agents/:id/stop | POST | Stop an agent |
| /market/orders | POST | Place order |
| /market/orders/:id | DELETE | Cancel order |
| /market/orderbook | GET | Get current orderbook |
| /market/loans | POST | Request loan |
| /risk/portfolio | GET | Get portfolio risk metrics |

## Environment Variables

Copy `.env.example` to `.env`:

```
PORT=3000
0G_CHAIN_ID=11155111
SEPOLIA_RPC_URL=https://sepolia.infura.io/v3/YOUR_KEY
ZERO_G_RPC_URL=https://0g-testnet-rpc.0g.network
ZERO_G_PRIVATE_KEY=your_0g_private_key
ZERO_G_STORAGE_RPC=https://storage.0g.ai
ZERO_G_DA_RPC=https://da.0g.ai
```

## Tech Stack

- **Node.js + TypeScript** - Runtime
- **Express.js** - Web server & API
- **ethers.js** - Blockchain interaction
- **WebSocket** - Real-time communication
- **0G SDK** - Storage integration

---

*Part of ColonAI ecosystem for 0G APAC Hackathon*
