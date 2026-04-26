---
sidebar_position: 3
---

# Agents Overview

ColonAI consists of six specialized AI agents, each with a unique trading strategy and responsibility.

## Agent Architecture

```
┌──────────────────────────────────────────────────────┐
│                  AGENT ECOSYSTEM                     │
│                                                      │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐         │
│  │  Scout   │──│ Momentum │──│  Swing   │         │
│  │  Agent   │  │  Agent   │  │  Agent   │         │
│  └──────────┘  └──────────┘  └──────────┘         │
│       ↓            ↓            ↓                   │
│       └────────────┼────────────┘                 │
│                    ↓                                │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐         │
│  │   Arb    │  │  Yield   │  │  Risk    │         │
│  │  Agent   │  │  Agent   │  │  Agent   │         │
│  └──────────┘  └──────────┘  └──────────┘         │
│                                                      │
└──────────────────────────────────────────────────────┘
```

## Agent Types

### 1. Scout Agent 🔎

**Role:** Market Scanner & Pattern Detection

**Strategy:**
- Detects trading opportunities using ML pattern recognition
- Monitors price movements, volume spikes, divergences
- Broadcasts signals to other agents

**Key Features:**
- Breakout detection
- Divergence analysis
- Volume spike identification
- Anomaly detection

**Timeframe:** 1H - 4H
**Capital Allocation:** 10%

[Learn more →](./scout-agent)

---

### 2. Momentum Agent ⚡

**Role:** Medium-term Trend Following

**Strategy:**
- EMA crossover (20/50)
- RSI confirmation
- Fibonacci pullback entries

**Key Features:**
- Trend alignment checks
- RSI overbought/oversold signals
- Fibonacci retracement levels

**Timeframe:** 4H - Daily
**Capital Allocation:** 20%

[Learn more →](./momentum-agent)

---

### 3. Swing Agent 🌊

**Role:** Medium-term Swing Trading

**Strategy:**
- MACD signals
- Bollinger Band breaks
- Support/Resistance levels

**Key Features:**
- Swing high/low detection
- Trend following
- Pullback entries

**Timeframe:** Daily - Weekly
**Capital Allocation:** 25%

[Learn more →](./swing-agent)

---

### 4. Arb Agent 💰

**Role:** Arbitrage Execution

**Strategy:**
- Cross-DEX arbitrage
- Internal market arbitrage
- Price discrepancy detection

**Key Features:**
- Real-time price monitoring
- Opportunity scoring
- Fast execution

**Timeframe:** Instant
**Capital Allocation:** 15%

[Learn more →](./arb-agent)

---

### 5. Yield Agent 🌾

**Role:** Yield Optimization

**Strategy:**
- Lending pool participation
- Staking rewards
- Yield farming

**Key Features:**
- Dynamic yield optimization
- Risk-adjusted returns
- Portfolio rebalancing

**Timeframe:** Ongoing
**Capital Allocation:** 20%

[Learn more →](./yield-agent)

---

### 6. Risk Agent 🛡️

**Role:** Portfolio Risk Management

**Strategy:**
- Position sizing limits
- Drawdown monitoring
- Risk override capability

**Key Features:**
- Max position limits per agent
- Stop-loss enforcement
- Portfolio-level risk monitoring
- Can override other agents' decisions

**Timeframe:** Real-time
**Capital Allocation:** 0% (oversees all)

[Learn more →](./risk-agent)

---

## Agent Communication

Agents communicate via two main channels:

### 1. 0G DA (Data Availability)

Real-time signal broadcasting:
- Scout → broadcasts signals to Momentum, Swing
- Arb → broadcasts arbitrage opportunities to Yield
- Risk → broadcasts risk alerts to all agents

### 2. Internal Market

Agent-to-agent trading:
- Scout sells signals → Momentum buys
- Arb sells opportunities → Yield buys
- Agents borrow/lend from Lending Pool

## Agent Reputation System

Each agent has an on-chain reputation score (0-1000):

- **High reputation** → More capital allocation, lower borrowing rates
- **Low reputation** → Less capital, higher borrowing rates

Reputation is updated when:
- Trades are profitable (+reputation)
- Stop-losses hit (-reputation)
- Agents consistently win/lose

## Next Steps

- 🤖 [Scout Agent Documentation](./scout-agent)
- ⚡ [Momentum Agent Documentation](./momentum-agent)
- 🌊 [Swing Agent Documentation](./swing-agent)
- 💰 [Arb Agent Documentation](./arb-agent)
- 🌾 [Yield Agent Documentation](./yield-agent)
- 🛡️ [Risk Agent Documentation](./risk-agent)
