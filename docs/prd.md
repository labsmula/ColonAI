# ColonAI — Product Requirements Document (PRD)

**Version:** 1.0
**Date:** April 23, 2026
**Hackathon:** 0G APAC Hackathon
**Track:** Autonomous Agent Economic Systems
**Team:** Mula Labs

---

## 1. Executive Summary

**ColonAI** adalah autonomous agent economic system yang berjalan di atas 0G Network. Ekosistem dari specialized trading agents yang memiliki wallet sendiri, berdagang secara mandiri maupun berkolaborasi, membagi profit melalui smart contract, dan dikelola melalui DAO governance.

**Tagline:** *The Colony That Trades Together*

**Token:** $COLON

---

## 2. Problem Statement

### 2.1 Problem

1. **Trading bots bekerja sendirian** — Tidak ada mekanisme kolaborasi antar bot. Setiap bot trade secara independen tanpa sinergi.
2. **Agent economy belum ada** — AI agents belum punya sistem ekonomi sendiri (wallet, kredit, profit sharing).
3. **Decision making terpusat** — Satu strategy = satu titik kegagalan. Multi-agent bisa mitigate risk.
4. **Transparansi rendah** — Trading bot proprietary, ga ada accountability. On-chain bisa solve ini.

### 2.2 Target Users

| User | Need |
|------|------|
| **Crypto Traders** | Passive income dari autonomous agents tanpa manage sendiri |
| **DeFi Protocols** | Need liquidity provider yang autonomous |
| **DAO Treasury** | Automated treasury management |
| **Developers** | Framework buat build specialized trading agents |

---

## 3. Product Vision

**ColonAI memungkinkan AI agents untuk:**
- Memiliki identitas on-chain (wallet, reputation)
- Berdagang secara mandiri di internal market & external DEX
- Berkolaborasi dengan agent lain (internal market, lending)
- Mendapatkan reward berdasarkan performa
- Dikontrol secara demokratis melalui DAO

**Long-term vision:** Menjadi *decentralized autonomous trading firm* — perusahaan trading yang seluruh operasinya dijalankan oleh AI agents, dimiliki oleh token holders.

---

## 4. Product Architecture

### 4.1 System Overview

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

### 4.2 Layer Descriptions

#### Layer 1: Dashboard (Frontend)
- **Tech:** Next.js + TailwindCSS + Recharts
- **Features:**
  - Real-time agent performance monitor
  - Live internal market orderbook
  - PnL breakdown per agent
  - DAO governance interface
  - Agent decision logs (explainable AI)

#### Layer 2: Orchestrator (Backend)
- **Tech:** Node.js + TypeScript + WebSocket
- **Features:**
  - Agent lifecycle management (deploy, start, stop)
  - Internal market order matching engine
  - Risk engine (portfolio-level monitoring)
  - Price feed aggregation
  - Event bus for agent communication

#### Layer 3: Agent Layer (AI Agents)
- **Tech:** Python + LangChain + OpenAI API (or 0G Compute for inference)
- **Features:**
  - 6 specialized agent types
  - Individual wallet & strategy
  - Memory system (0G Storage KV Layer)
  - Inter-agent communication protocol

#### Layer 4: 0G Network (Blockchain)
- **0G Chain:** Smart contracts (Solidity)
- **0G Storage:** Agent data, trade history, ML models
- **0G Compute:** Model inference (future)
- **0G DA:** Fast agent coordination data

---

## 5. Agent Specifications

### 5.1 Scout Agent (Market Scanner)

| Property | Value |
|----------|-------|
| **Role** | Scan market, identify opportunities |
| **Timeframe** | Continuous |
| **Strategy** | Pattern recognition, anomaly detection |
| **Output** | Signal broadcast ke semua agents |
| **Risk** | N/A (no trading, only analysis) |
| **0G Usage** | Storage (market data cache), DA (broadcast signals) |

**Behavior:**
1. Monitor real-time price feeds
2. Detect patterns (breakout, divergence, unusual volume)
3. Broadcast signals ke Momentum & Swing agents
4. Log findings ke 0G Storage

### 5.2 Momentum Agent

| Property | Value |
|----------|-------|
| **Role** | Short-term momentum trading |
| **Timeframe** | 1m - 15m charts |
| **Strategy** | EMA crossover + RSI + volume confirmation |
| **Risk Budget** | 1% per trade, max 3 open positions |
| **Capital Allocation** | 20% dari total treasury |

**Behavior:**
1. Receive signal dari Scout Agent
2. Confirm dengan technical indicators
3. Execute trade di internal market atau MockDEX
4. Auto SL/TP management
5. Report trade ke Orchestrator

### 5.3 Swing Agent

| Property | Value |
|----------|-------|
| **Role** | Medium-term trend trading |
| **Timeframe** | 4H - Daily |
| **Strategy** | Trend following + Fibonacci pullback |
| **Risk Budget** | 2% per trade, max 2 open positions |
| **Capital Allocation** | 30% dari total treasury |

**Behavior:**
1. Analyze higher timeframe trends
2. Wait for pullback entry
3. Execute with limit orders
4. Trail stop loss
5. Longer hold period (2-7 days)

### 5.4 Arb Agent (Arbitrage)

| Property | Value |
|----------|-------|
| **Role** | Internal market arbitrage + price discrepancies |
| **Timeframe** | Real-time |
| **Strategy** | Internal price discrepancy + MockDEX spread |
| **Risk Budget** | 0.5% per trade |
| **Capital Allocation** | 15% dari total treasury |

**Behavior:**
1. Monitor internal market orderbook
2. Detect price discrepancy antar agents
3. Execute arbitrage trade (buy low, sell high)
4. Also lend idle capital ke agents yang butuh (interest income)

### 5.5 Yield Agent

| Property | Value |
|----------|-------|
| **Role** | Deploy idle capital ke yield sources |
| **Timeframe** | Hourly - Daily rebalancing |
| **Strategy** | Automated capital reallocation |
| **Risk Budget** | Conservative (no leverage) |
| **Capital Allocation** | 25% dari total treasury |

**Behavior:**
1. Identify idle capital across agents
2. Move idle funds ke highest yield internal pool
3. Provide liquidity ke internal market
4. Report yield earned

### 5.6 Risk Agent (Portfolio Guardian)

| Property | Value |
|----------|-------|
| **Role** | Portfolio-level risk management |
| **Timeframe** | Continuous |
| **Strategy** | VaR, correlation analysis, hedging |
| **Risk Budget** | Override all agents if needed |
| **Capital Allocation** | 10% (hedging reserve) |

**Behavior:**
1. Monitor total portfolio exposure
2. Check correlated positions
3. If portfolio risk > threshold → force reduce
4. Can override other agents' decisions (emergency)
5. Report risk metrics ke dashboard

---

## 6. Smart Contracts

### 6.1 Contract Architecture

```
contracts/
├── core/
│   ├── ColonToken.sol          // $COLON ERC-20 token
│   ├── AgentRegistry.sol       // Agent identity & reputation
│   └── Treasury.sol            // Fund management
├── market/
│   ├── InternalMarket.sol      // Agent-to-agent trading
│   ├── OrderBook.sol           // Order matching engine
│   └── MockDEX.sol             // Simulated external DEX
├── economy/
│   ├── ProfitDistributor.sol   // Profit sharing logic
│   ├── LendingPool.sol         // Agent-to-agent lending
│   └── Escrow.sol              // Trustless payments
└── governance/
    ├── ColonyDAO.sol           // Proposal & voting
    └── Timelock.sol            // Execution delay
```

### 6.2 ColonToken ($COLON)

```solidity
// ERC-20 Token with governance capabilities
- Total Supply: 10,000,000 $COLON
- Distribution:
  - 40% — Community (staking rewards)
  - 25% — Treasury (agent capital)
  - 20% — Team & Development
  - 10% — Hackathon Prize
  - 5%  — Initial Liquidity
```

### 6.3 AgentRegistry

```solidity
struct Agent {
    address wallet;
    string name;
    AgentType agentType;    // enum: SCOUT, MOMENTUM, SWING, ARB, YIELD, RISK
    uint256 reputation;     // 0-1000 score
    uint256 totalProfit;
    uint256 totalTrades;
    uint256 winRate;        // basis points (5000 = 50%)
    bool isActive;
}

// Functions
- registerAgent(name, type) → creates agent profile
- updateReputation(agentId, delta) → called after trade
- getTopPerformers(limit) → leaderboard query
- deactivateAgent(agentId) → governance only
```

### 6.4 InternalMarket

```solidity
enum OrderSide { BUY, SELL }
enum OrderType { MARKET, LIMIT }

struct Order {
    address agent;
    OrderSide side;
    OrderType type;
    address tokenIn;
    address tokenOut;
    uint256 amount;
    uint256 price;
    uint256 timestamp;
}

// Matching Engine Logic
- placeOrder(order) → emit event, try match
- cancelOrder(orderId) → agent cancels own order
- matchOrders(buyOrder, sellOrder) → atomic swap via escrow
- getFilledOrders(agent) → trade history query
```

### 6.5 ProfitDistributor

```solidity
// Called by Orchestrator at end of epoch (daily)
function distributeProfits(uint256 epochId) {
    uint256 totalProfit = _calculateEpochProfit(epochId);
    
    // Distribution splits
    uint256 agentShare = totalProfit * 40 / 100;   // 40% to performing agents
    uint256 treasuryCut = totalProfit * 30 / 100;   // 30% to treasury
    uint256 rewardPool = totalProfit * 20 / 100;    // 20% to staking rewards
    uint256 holderReward = totalProfit * 10 / 100;   // 10% to $COLON stakers
}
```

### 6.6 LendingPool

```solidity
struct Loan {
    address borrower;
    address lender;
    uint256 amount;
    uint256 interestRate;  // basis points per day
    uint256 startTime;
    uint256 duration;
    bool repaid;
}

// Functions
- requestLoan(amount, duration) → agent requests capital
- fundLoan(loanId) → another agent funds it
- repayLoan(loanId) → borrower returns + interest
- liquidateLoan(loanId) → if overdue, lender can claim collateral
```

### 6.7 ColonyDAO

```solidity
enum ProposalType {
    ADD_AGENT_TYPE,
    UPDATE_STRATEGY,
    ADJUST_LEVERAGE,
    TREASURY_SPEND,
    PARAMETER_CHANGE
}

struct Proposal {
    address proposer;
    ProposalType proposalType;
    string description;
    uint256 votesFor;
    uint256 votesAgainst;
    uint256 deadline;
    bool executed;
}

// Voting: 1 $COLON = 1 vote (quadratic for large holders)
- createProposal(type, description)
- castVote(proposalId, support)
- executeProposal(proposalId) → after deadline + timelock
```

---

## 7. Orchestrator Design

### 7.1 Component Architecture

```
orchestrator/
├── agents/
│   ├── base-agent.ts         // Base class for all agents
│   ├── scout-agent.ts
│   ├── momentum-agent.ts
│   ├── swing-agent.ts
│   ├── arb-agent.ts
│   ├── yield-agent.ts
│   └── risk-agent.ts
├── market/
│   ├── internal-market.ts    // Order matching engine
│   ├── mock-dex.ts           // Simulated DEX
│   └── price-feed.ts         // Price data provider
├── risk/
│   ├── risk-engine.ts        // Portfolio risk calculator
│   └── position-manager.ts   // Track all open positions
├── communication/
│   ├── event-bus.ts          // Inter-agent messaging
│   └── signal-broadcaster.ts // Scout → Trader communication
├── chain/
│   ├── contract-interaction.ts // Smart contract calls
│   └── wallet-manager.ts     // Agent wallet management
└── storage/
    ├── trade-logger.ts       // Log trades to 0G Storage
    └── agent-memory.ts       // KV store for agent state
```

### 7.2 Agent Communication Protocol

```
Event Types:
├── SIGNAL_DETECTED     // Scout → Momentum/Swing (new opportunity)
├── TRADE_EXECUTED      // Any agent → Orchestrator (trade done)
├── RISK_ALERT          // Risk Agent → All (reduce exposure)
├── LOAN_REQUEST        // Any agent → Market (need capital)
├── LOAN_FUNDED         // Lender → Borrower (capital sent)
├── PROFIT_DISTRIBUTED  // Contract → Dashboard (epoch ended)
└── GOVERNANCE_UPDATE   // DAO → All (parameter change)
```

### 7.3 Decision Flow

```
[Price Feed Update]
       ↓
[Scout Agent] → analyze → detect pattern?
       ↓ YES
[Broadcast Signal]
       ↓
[Momentum Agent] ← receive signal
       ↓
[Confirm with Indicators] → execute?
       ↓ YES
[Check with Risk Agent] → approved?
       ↓ YES
[Place Order on Internal Market]
       ↓
[Order Matched]
       ↓
[Execute Trade] → log to 0G Storage
       ↓
[Update Agent Reputation]
       ↓
[Risk Agent recalculates portfolio]
```

---

## 8. Dashboard Design

### 8.1 Pages

| Page | Description |
|------|-------------|
| **Overview** | Total portfolio PnL, agent count, active trades, market status |
| **Agents** | Individual agent cards: name, type, PnL, win rate, reputation, recent trades |
| **Market** | Live internal market orderbook + trade history |
| **Lending** | Active loans, interest rates, pool liquidity |
| **Governance** | Active proposals, voting interface, proposal history |
| **Analytics** | Charts: PnL over time, agent comparison, risk metrics |

### 8.2 Key Metrics (Overview)

```
┌─────────────────────────────────────────────────────────┐
│  🐜 ColonAI Dashboard                                    │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  Total Portfolio     $5,230      +4.6% (24h)           │
│  Active Agents       6/6         🟢 All Running          │
│  Open Trades         8           3 Buy / 5 Sell          │
│  Internal Market     $12,400     Volume (24h)            │
│  Active Loans        3           $800 Lent               │
│  DAO Proposals       1           Voting Now               │
│                                                         │
│  ┌─────────────┐ ┌─────────────┐ ┌─────────────┐      │
│  │ 📊 Scout    │ │ ⚡ Momentum │ │ 📈 Swing    │      │
│  │ Signals: 12 │ │ PnL: +$120 │ │ PnL: +$85  │      │
│  │ 🟢 Active  │ │ Win: 72%   │ │ Win: 65%   │      │
│  └─────────────┘ └─────────────┘ └─────────────┘      │
│                                                         │
│  ┌─────────────┐ ┌─────────────┐ ┌─────────────┐      │
│  │ 🔄 Arb     │ │ 💰 Yield   │ │ 🛡️ Risk    │      │
│  │ PnL: +$200 │ │ Yield: 2.1%│ │ VaR: 3.2%  │      │
│  │ Win: 89%   │ │ 🟢 Active │ │ 🟢 Safe    │      │
│  └─────────────┘ └─────────────┘ └─────────────┘      │
│                                                         │
│  [PnL Chart ──────────────────────── 24h/7d/30d]       │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

---

## 9. 0G Integration Map

| 0G Service | Usage | Data Type | Access Pattern |
|------------|-------|-----------|----------------|
| **0G Chain** | Smart contracts | Agent registry, trades, governance | Write (on-chain tx) |
| **0G Storage (Log)** | Trade history, audit logs | Append-only records | Write heavy, read occasionally |
| **0G Storage (KV)** | Agent state, memory, settings | Structured key-value | Read/write frequently |
| **0G Compute** | ML inference (future phase) | Model predictions | Read-only (inference) |
| **0G DA** | Agent coordination signals | Small messages, fast | Write + read, low latency |

---

## 10. Demo Plan (Hackathon)

### 10.1 Demo Duration: 10 minutes

| Time | Section | Content |
|------|---------|---------|
| 0:00-1:00 | **Intro** | Problem statement, ColonAI vision |
| 1:00-2:00 | **Architecture** | System overview diagram, 0G integration |
| 2:00-4:00 | **Live Demo** | Deploy agents, watch them trade live on dashboard |
| 4:00-5:30 | **Internal Market** | Show orderbook, agent-to-agent trade, lending |
| 5:30-6:30 | **Risk & Governance** | Risk agent override, DAO proposal demo |
| 6:30-8:00 | **Smart Contracts** | Walk through key contracts on 0G explorer |
| 8:00-9:00 | **Differentiation** | Why ColonAI > single trading bot |
| 9:00-10:00 | **Roadmap & Q&A** | Future plans, open for questions |

### 10.2 Demo Requirements

- [ ] All 6 agents running & trading
- [ ] Dashboard showing live PnL
- [ ] At least 1 agent-to-agent trade visible
- [ ] At least 1 internal loan active
- [ ] 1 DAO proposal created & voted
- [ ] Smart contracts deployed on 0G testnet
- [ ] Trade logs visible on 0G Storage

---

## 11. Technical Requirements

### 11.1 Tech Stack

| Component | Technology | Version |
|-----------|-----------|---------|
| **Smart Contracts** | Solidity | ^0.8.24 |
| **Contract Framework** | Hardhat | Latest |
| **Backend** | Node.js + TypeScript | Node 20+ |
| **Agent Framework** | Python + LangChain | Python 3.11+ |
| **Frontend** | Next.js + TailwindCSS | Next.js 14+ |
| **Charts** | Recharts | Latest |
| **Chain Interaction** | ethers.js | v6+ |
| **Testing** | Chai + Mocha (contracts), Jest (backend) | Latest |

### 11.2 Infrastructure

| Service | Provider | Purpose |
|---------|----------|---------|
| **Blockchain** | 0G Network (testnet) | Smart contract deployment |
| **Storage** | 0G Storage | Agent data & trade logs |
| **Compute** | 0G Compute (optional) | ML inference |
| **Hosting** | Vercel (frontend) | Dashboard hosting |
| **Backend** | Railway / Fly.io | Orchestrator hosting |
| **RPC** | 0G testnet RPC | Blockchain interaction |

### 11.3 Dependencies (contracts)

```json
{
  "@openzeppelin/contracts": "^5.0.0",
  "@openzeppelin/contracts-upgradeable": "^5.0.0"
}
```

### 11.4 Dependencies (backend)

```json
{
  "ethers": "^6.0.0",
  "ws": "^8.0.0",
  "express": "^4.18.0",
  "dotenv": "^16.0.0",
  "cors": "^2.8.5"
}
```

---

## 12. Milestones & Timeline

### Phase 1: Foundation (Week 1-2)
- [ ] Smart contract development (all 7 contracts)
- [ ] Contract testing & deployment to 0G testnet
- [ ] Basic orchestrator setup
- [ ] Price feed integration

### Phase 2: Agent Development (Week 2-3)
- [ ] Base agent class & communication protocol
- [ ] Scout Agent implementation
- [ ] Momentum Agent implementation
- [ ] Swing Agent implementation
- [ ] Risk Agent implementation

### Phase 3: Market & Economy (Week 3-4)
- [ ] Internal market matching engine
- [ ] MockDEX implementation
- [ ] Lending pool logic
- [ ] Profit distribution logic

### Phase 4: Dashboard & Demo (Week 4-5)
- [ ] Dashboard UI (all 6 pages)
- [ ] Real-time data feed (WebSocket)
- [ ] DAO governance interface
- [ ] Demo preparation & rehearsal

### Phase 5: Submission (Week 5-6)
- [ ] Final testing & bug fixes
- [ ] Documentation
- [ ] Video recording
- [ ] Submit to HackQuest

---

## 13. Success Metrics (Hackathon Judging)

| Criteria | How ColonAI Addresses |
|----------|----------------------|
| **Innovation** | First multi-agent cooperative trading system on 0G |
| **Technical Complexity** | 7 smart contracts + 6 AI agents + real-time orchestration |
| **0G Integration** | Full stack: Chain + Storage + DA (+ Compute future) |
| **Demo Quality** | Live dashboard with real-time agent trading |
| **Practicality** | Real use case (autonomous trading firm) |
| **Code Quality** | Clean architecture, tested contracts, documented |

---

## 14. Risks & Mitigations

| Risk | Probability | Impact | Mitigation |
|------|------------|--------|------------|
| 0G testnet instability | Medium | High | Mock fallback for demo |
| Agent AI hallucination | High | Medium | Risk Agent override + human kill switch |
| Smart contract bugs | Low | Critical | Audit + testnet deployment |
| Price feed delay | Medium | Medium | Multiple feed sources + caching |
| Demo failure | Low | Critical | Pre-recorded backup + extensive rehearsal |
| Complexity overload | High | High | MVP-first approach (start with 3 agents) |

---

## 15. Future Roadmap

### Post-Hackathon
1. **Real DEX integration** — Connect to actual Uniswap/0x for live trading
2. **0G Compute ML inference** — Run prediction models on 0G GPU network
3. **Mobile app** — Portfolio monitoring on-the-go
4. **Strategy marketplace** — Let users create & sell agent strategies
5. **Cross-chain** — Multi-chain trading (Ethereum, Solana, etc.)
6. **ZK proofs** — Privacy-preserving strategy verification

---

## 16. Appendices

### A. Glossary
- **Colony** — Group of autonomous agents in ColonAI
- **Internal Market** — Agent-to-agent trading venue within ColonAI
- **Scout** — Non-trading agent that scans for opportunities
- **Reputation Score** — On-chain metric (0-1000) based on agent performance
- **Epoch** — Time period (24h) for profit distribution

### B. References
- 0G Documentation: https://docs.0g.ai/
- TradingAgents Paper: https://tradingagents-ai.github.io/
- AgentDAO: https://github.com/Tonyflam/agentdao
- 0G Whitepaper: https://cdn.jsdelivr.net/gh/0glabs/0g-doc/static/whitepaper.pdf

---

*Built with 🐜 by Mula Labs for 0G APAC Hackathon*
