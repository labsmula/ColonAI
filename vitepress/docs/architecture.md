---
sidebar_position: 4
---

# Architecture

ColonAI is a 4-layer decentralized autonomous trading system.

## System Overview

```
┌──────────────────────────────────────────────────────────────┐
│                     COLONAI ECOSYSTEM                        │
│                                                              │
│  ┌──────────────────────────────────────────────────────┐   │
│  │                 DASHBOARD (Frontend)                  │   │
│  │   Agent Monitor │ Market View │ Governance │ PnL      │   │
│  └──────────────────────┬───────────────────────────────┘   │
│                          ↓                                   │
│  ┌──────────────────────────────────────────────────────┐   │
│  │              ORCHESTRATOR (Backend)                   │   │
│  │   Agent Manager │ Market Maker │ Risk Engine          │   │
│  └──────────────────────┬───────────────────────────────┘   │
│                          ↓                                   │
│  ┌──────────────────────────────────────────────────────┐   │
│  │              AGENT LAYER (AI Agents)                  │   │
│  │  ┌──────────┐┌──────────┐┌──────────┐┌──────────┐   │   │
│  │  │  Scout   ││ Momentum ││  Swing   ││   Arb    │   │   │
│  │  │  Agent   ││  Agent   ││  Agent   ││  Agent   │   │   │
│  │  └──────────┘└──────────┘└──────────┘└──────────┘   │   │
│  │  ┌──────────┐┌──────────┐                           │   │
│  │  │  Yield   ││  Risk    │                           │   │
│  │  │  Agent   ││  Agent   │                           │   │
│  │  └──────────┘└──────────┘                           │   │
│  └──────────────────────┬───────────────────────────────┘   │
│                          ↓                                   │
│  ┌──────────────────────────────────────────────────────┐   │
│  │              0G NETWORK (Infrastructure)              │   │
│  │  ┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐               │   │
│  │  │ Chain│ │Store │ │Compute│ │  DA  │               │   │
│  │  └──────┘ └──────┘ └──────┘ └──────┘               │   │
│  └──────────────────────────────────────────────────────┘   │
└──────────────────────────────────────────────────────────────┘
```

## Layer 1: Dashboard (Frontend)

**Tech Stack:** Next.js + TailwindCSS + Recharts

**Components:**
- **Agent Monitor** — Real-time performance metrics for each agent
- **Market View** — Live internal market orderbook
- **Governance** — ColonyDAO proposal & voting interface
- **PnL Dashboard** — Portfolio performance & profit distribution

**Key Features:**
- WebSocket real-time updates
- Interactive charts (PnL, Win Rate, Drawdown)
- Responsive design (mobile-friendly)

---

## Layer 2: Orchestrator (Backend)

**Tech Stack:** Node.js + Express + ethers.js

**Components:**

### Agent Manager
- Agent lifecycle (start/stop/restart)
- Agent state management
- Agent reputation tracking

### Market Maker
- Internal market order matching
- Price discovery
- Orderbook management

### Risk Engine
- Position size enforcement
- Stop-loss monitoring
- Portfolio-level risk checks

---

## Layer 3: Agent Layer (AI Agents)

**Tech Stack:** Python + LangChain + OpenAI

**Six Specialized Agents:**

| Agent | Strategy | Timeframe | Capital |
|-------|----------|-----------|---------|
| Scout | Pattern detection | 1H-4H | 10% |
| Momentum | EMA+RSI trend following | 4H-Daily | 20% |
| Swing | MACD swing trading | Daily-Weekly | 25% |
| Arb | Arbitrage execution | Instant | 15% |
| Yield | Yield optimization | Ongoing | 20% |
| Risk | Portfolio risk management | Real-time | 0% |

**Communication:**
- 0G DA — Real-time signal broadcasting
- Internal Market — Agent-to-agent trading

---

## Layer 4: 0G Network (Infrastructure)

| 0G Service | Usage | Implementation Status |
|------------|-------|------------------------|
| **0G Chain** | Smart contracts, agent wallets | 🟢 Active |
| **0G Storage** | Trade history, reputation data | 🟢 Active |
| **0G Compute** | Agent inference | 🟡 Future |
| **0G DA** | Agent coordination, orderbook | 🟢 Active |

---

## Data Flow

### 1. Signal Detection
```
Scout Agent → Detects breakout → Broadcasts via 0G DA
                                          ↓
                                  Momentum Agent receives
                                          ↓
                                  Analyzes & executes trade
```

### 2. Trade Execution
```
Agent → Internal Market → Order Placed
                                  ↓
                          Market Maker matches
                                  ↓
                          Treasury allocates funds
                                  ↓
                          Trade executed on-chain
```

### 3. Profit Distribution
```
Trade completed → Profit calculated
                              ↓
                      Smart contract distributes:
                      - 40% to executing agent
                      - 30% to Treasury
                      - 20% to signal provider
                      - 10% to $COLON buyback
```

---

## Smart Contract Layer

| Contract | Purpose | Status |
|----------|---------|--------|
| **ColonToken** | $COLON ERC-20 | 🟢 Deployed |
| **AgentRegistry** | Agent registration & reputation | 🟢 Deployed |
| **Treasury** | Fund management | 🟢 Deployed |
| **InternalMarket** | Orderbook & matching | 🟢 Deployed |
| **LendingPool** | Agent-to-agent lending | 🟡 Development |
| **ProfitDistributor** | Profit sharing | 🟡 Development |
| **ColonyDAO** | Governance | 🟡 Development |

---

## Security Considerations

- ✅ Smart contracts audited (before mainnet deployment)
- ✅ Agent actions require wallet signature
- ✅ Risk Agent can override any trade
- ✅ 24-hour timelock for DAO proposals
- ✅ Emergency pause mechanism

## Next Steps

- 🤖 [Agents Overview](./agents) — Learn about each agent
- 💰 [Internal Market](./market-overview) — Explore the marketplace
- 📜 [Smart Contracts](./contracts-overview) — Understand the on-chain logic
