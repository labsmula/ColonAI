# AutoHive — Complete Project Specification

## Project Overview
Autonomous trading agent ecosystem where agents own wallets, trade independently or cooperatively, share profits, and are governed by DAO.

## Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                    AUTOHIVE ECOSYSTEM                  │
└─────────────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────────────┐
│                    AGENT LAYER                        │
├─────────────────────────────────────────────────────────────────┤
│ ┌──────────┐ ┌──────────┐ ┌──────────┐           │
│ │ScalpAgent│ │SwingAgent│ │ ArbAgent │           │
│ │ (HF)     │ (Mid)     │ (Arb)    │           │
│ └─────┬────┘ └─────┬────┘ └─────┬────┘           │
│       │              │              │              │               │
│       └──────────────┴──────────────┴──────────────┘               │
│                      ↓                                             │
│              ┌─────────────────┐                                 │
│              │  Internal Market│                                 │
│              └────────┬────────┘                                 │
└─────────────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────────────┐
│               0G BLOCKCHAIN LAYER                     │
├─────────────────────────────────────────────────────────────────┤
│  Agent Registry │ Profit Sharing │ DAO Governance          │
└─────────────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────────────┐
│               0G STORAGE & COMPUTE                    │
├─────────────────────────────────────────────────────────────────┤
│  Trade History | Agent Memory | ML Models | Market Data   │
└─────────────────────────────────────────────────────────────────┘
```

## Agent Types

### 1. ScalpAgent (High-Frequency)
- Timeframe: 1-5m
- Strategy: Breakout + momentum
- Risk: Aggressive (max 5%/trade)

### 2. SwingAgent (Medium-Term)
- Timeframe: 4H - Daily
- Strategy: Trend following + pullback
- Risk: Moderate (max 2%/trade)

### 3. ArbAgent (Arbitrage)
- Timeframe: Real-time
- Strategy: Cross-exchange arbitrage
- Risk: Low (execution risk)

### 4. YieldAgent (DeFi)
- Timeframe: Hourly
- Strategy: Yield farming
- Risk: Conservative

### 5. RiskAgent (Portfolio Manager)
- Timeframe: Continuous
- Strategy: VaR + hedging
- Risk: Defensive

## Economic Model

### Initial Agent Setup
- Wallet on 0G Chain
- Initial capital: $1000 from treasury
- Max leverage: 3x (DAO-set)
- Reputation score: 100

### Profit Sharing (Smart Contract)
```
40% → Agent that generated trade
30% → Treasury (re-investment)
20% → Reward pool (new agents)
10% → Governance token holders
```

### Agent-to-Agent Loans
- Dynamic interest: 0.1-1%/day
- Based on supply/demand
- Escrowed by smart contract

## DAO Governance

### Voting Power
- 1-99 $HIVE: 1 vote
- 100-999 $HIVE: 10 votes
- 1000+ $HIVE: 100 votes

### Proposal Types
- Strategy changes
- New agent types
- Treasury allocation
- Parameter adjustments

## References
- TradingAgents: https://tradingagents-ai.github.io/
- AgentDAO: https://github.com/Tonyflam/agentdao
- AgentDAO Demo: https://youtu.be/Cx2LNIND8RI

## 0G Stack Usage

### 0G Chain
- Agent registry smart contracts
- Profit distribution
- DAO governance

### 0G Storage
- Agent strategies (KV Layer)
- Trade history (Log Layer)
- ML models

### 0G Compute
- ML model inference
- Real-time predictions

### 0G DA
- Fast agent coordination
- Internal market communication
