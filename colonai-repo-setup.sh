#!/bin/bash

# ColonAI Repository Setup Script
# Run this in /root/.openclaw/workspace-colonai/

set -e

# Configuration
PROJECT_NAME="ColonAI"
GITHUB_USERNAME="zakkiye14"
REPO_NAME="colonai"
DESCRIPTION="Autonomous Agent Economic System on 0G Network"

echo "🚀 Setting up $PROJECT_NAME repository..."

# Create project structure
mkdir -p contracts orchestrator dashboard agents docs

# Initialize git (if not already initialized)
if [ ! -d ".git" ]; then
    git init
    echo "✅ Git repository initialized"
else
    echo "✅ Git already initialized"
fi

# Create .gitignore
cat > .gitignore << 'EOF'
# Dependencies
node_modules/
.env
.DS_Store

# Hardhat
artifacts/
cache/
typechain/
coverage/

# Python
__pycache__/
*.py[cod]
venv/
.venv/

# IDE
.vscode/
.idea/

# Environment
.env.local
*.log
EOF
echo "✅ Created .gitignore"

# Create LICENSE (MIT)
cat > LICENSE << 'EOF'
MIT License

Copyright (c) 2026 Mula Labs

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights to use,
copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
EOF
echo "✅ Created LICENSE (MIT)"

# Create README.md
cat > README.md << 'EOF'
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
EOF
echo "✅ Created README.md"

# Create initial subdirectories with README
mkdir -p contracts/README.md orchestrator/README.md dashboard/README.md agents/README.md docs/README.md

echo "# Contracts" > contracts/README.md
echo "# Orchestrator (Backend)" > orchestrator/README.md
echo "# Dashboard (Frontend)" > dashboard/README.md
echo "# Agents (Python)" > agents/README.md
echo "# Documentation" > docs/README.md

echo ""
echo "✅ Repository structure created!"
echo ""
echo "Next steps:"
echo "1. cd contracts && npm install (setup Hardhat)"
echo "2. cd orchestrator && npm install (setup backend)"
echo "3. cd dashboard && npm install (setup frontend)"
echo "4. cd agents && pip install langchain openai (setup agents)"
