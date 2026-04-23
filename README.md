# 🐜 ColonAI

**The Colony That Trades Together**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![0G APAC Hackathon](https://img.shields.io/badge/0G-APAC-2026-blue.svg)](https://www.hackquest.io/hackathons/0G-APAC-Hackathon)
[![Track: Agent Economics](https://img.shields.io/badge/Track-Agent%20Economics-green.svg)](https://www.hackquest.io/hackathons/0G-APAC-Hackathon)

> An autonomous agent economic system built on 0G Network where specialized trading agents own wallets, cooperate, and share profits through smart contracts.

## 📋 Overview

ColonAI is a multi-agent trading ecosystem where AI agents:
- Own individual wallets on-chain
- Trade independently or cooperatively
- Share profits via smart contracts
- Governed by DAO

## 🏗️ Architecture

\`\`\`
┌─────────────────────────────────────────────────┐
│                COLONAI ECOSYSTEM            │
├─────────────────────────────────────────────────┤
│ Dashboard │ Orchestrator │ Agents │ 0G Network│
└─────────────────────────────────────────────────┘
\`\`\`

## 🤖 Agent Types

| Agent | Role | Strategy |
|--------|-------|----------|
| Scout | Market scanner | Pattern detection |
| Momentum | HF trading | EMA + RSI |
| Swing | Medium-term | Trend following |
| Arb | Arbitrage | Price discrepancy |
| Yield | DeFi farming | Auto-rebalance |
| Risk | Portfolio guardian | VaR + hedging |

## 💸 Economic Model

- **40%** → Performing agents
- **30%** → Treasury (re-invest)
- **20%** → Reward pool
- **10%** → Token holders

## 🔗 Tech Stack

| Component | Tech |
|-----------|-------|
| Smart Contracts | Solidity + Hardhat |
| Backend | Node.js + TypeScript + ethers.js |
| Agents | Python + LangChain + OpenAI |
| Frontend | Next.js + TailwindCSS + Recharts |
| 0G | Chain + Storage + DA integration |

## 🚀 Quick Start

### Prerequisites

\`\`\`bash
npm install -g pnpm@latest git
\`\`\`

### Installation

\`\`\`bash
# Install contracts
cd contracts && npm install

# Install orchestrator (backend)
cd orchestrator && npm install

# Install dashboard (frontend)
cd dashboard && npm install

# Install agents
cd agents && pip install langchain openai
\`\`\`

### Development

\`\`\`bash
# Run contracts (Hardhat)
cd contracts && npx hardhat node

# Run orchestrator (backend)
cd orchestrator && npm run dev

# Run dashboard (frontend)
cd dashboard && npm run dev
\`\`\`

## 📊 Demo Plan

| Time | Section |
|------|---------|
| 0:00-1:00 | Intro & Vision |
| 1:00-2:00 | Architecture Overview |
| 2:00-4:00 | Live Demo — Agents Trading |
| 4:00-5:30 | Internal Market & Lending |
| 5:30-6:30 | Risk & Governance |
| 6:30-8:00 | Smart Contracts Deep Dive |
| 8:00-9:00 | Differentiation & Roadmap |
| 9:00-10:00 | Q&A |

## 📝 Documentation

- **[PRD](docs/prd.md)** — Complete product requirements
- **[Architecture](docs/architecture.md)** — System design
- **[API](docs/api.md)** — API documentation
- **[Smart Contracts](docs/contracts.md)** — Contract documentation

## 🏆 Team

Built by **Mula Labs** for 0G APAC Hackathon

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
