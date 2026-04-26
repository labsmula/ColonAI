---
sidebar_position: 2
---

# Getting Started

This guide will help you set up the ColonAI development environment and run the agents locally.

## Prerequisites

- **Node.js** >= 18.0.0
- **Python** >= 3.9
- **npm** or **yarn**

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/labsmula/ColonAI.git
cd ColonAI
```

### 2. Install Backend Dependencies

```bash
cd orchestrator
npm install
```

### 3. Install Python Dependencies

```bash
cd ../agents
pip install -r requirements.txt
```

### 4. Configure Environment Variables

```bash
cd ../orchestrator
cp .env.example .env
```

Edit `.env` and add your configurations:

```env
# 0G Configuration
OG_CHAIN_RPC_URL=https://testnet.0gchain.io
OG_PRIVATE_KEY=your_private_key_here

# OpenAI API (optional - for AI agents)
OPENAI_API_KEY=your_openai_key_here

# Server Configuration
PORT=3000
```

## Running the System

### Start the Orchestrator

The Orchestrator is the backend server that coordinates all agents.

```bash
cd orchestrator
npm start
```

The Orchestrator will start on `http://localhost:3000`.

### Run an Agent

Agents can be run independently. Here's how to run the Scout Agent:

```bash
cd agents
python scout-agent.py
```

### Run Multiple Agents

To run all agents simultaneously, use the provided script:

```bash
cd agents
./run-all-agents.sh
```

## Development Workflow

### 1. Run Tests

```bash
# Backend tests
cd orchestrator
npm test

# Agent tests
cd agents
python -m pytest tests/
```

### 2. Build Smart Contracts

```bash
cd contracts
npx hardhat compile
```

### 3. Deploy to 0G Testnet

```bash
cd contracts
npx hardhat deploy --network 0g-testnet
```

## Troubleshooting

### Port 3000 Already in Use

If port 3000 is already in use, change it in `orchestrator/.env`:

```env
PORT=3001
```

### Agent Connection Failed

Make sure the Orchestrator is running:

```bash
curl http://localhost:3000/health
```

### 0G Network Connection Failed

Check your 0G testnet configuration in `.env` and ensure you have testnet tokens.

## Next Steps

- 🏗️ [Architecture](./architecture) — Understand the system design
- 🤖 [Agents](./agents) — Learn about each specialized agent
- 💰 [Internal Market](./market-overview) — Explore the agent-to-agent marketplace

---

Need help? Join our [Discord](https://discord.com/invite/clawd) or create a [GitHub Issue](https://github.com/labsmula/ColonAI/issues).
