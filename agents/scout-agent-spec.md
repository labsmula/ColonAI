# Scout Agent Specification

## Overview
Scout Agent is a market scanner that detects trading opportunities and broadcasts signals to Momentum and Swing agents.

## Agent Type
- **ID:** scout_agent_001
- **Type:** SCOUT
- **Role:** Market scanner & pattern detection
- **Target Agents:** Momentum, Swing

## Capabilities

### 1. Pattern Detection
Detects trading patterns using ML model:
- **Breakout** — Strong momentum movements (>5% in 1h)
- **Divergence** — RSI divergence patterns (>3% change)
- **Volume Spike** — Unusual volume activity (>2x average)
- **Anomaly** — Abnormal price movements

### 2. Signal Broadcasting
Broadcasts detected signals to Momentum and Swing agents:
- Signal type (BREAKOUT, DIVERGENCE, VOLUME_SPIKE, ANOMALY)
- Symbol, direction, confidence score
- Reasoning for the signal

### 3. 0G Integration
| 0G Service | Usage |
|------------|-------|
| Storage (KV) | Cache market data, log signal history |
| DA | Broadcast signals in real-time |

### 4. Reputation System
- Starting score: 1000 (0-1000 scale)
- Updated when signals confirmed by trading agents
- Future: Implement decay over time

## Architecture

```
┌─────────────────────────────────────────────────┐
│ Scout Agent (Python)                          │
├─────────────────────────────────────────────────┤
│  ┌──────────────┐ ┌──────────────┐    │
│  │ Pattern Engine│ Signal Broadcast│   │    │
│  └──────────────┘ └──────────────┘    │
└─────────────────────────────────────────────────┘
         ↓                    ↓
┌─────────────────────────────────────────────────┐
│              0G Network (Infrastructure)         │
│  ┌──────────────┐ ┌──────────────┐    │
│  │ 0G Storage  │   0G DA        │    │
│  │ (KV Cache)    │   (Real-time)   │    │
│  └──────────────┘ └──────────────┘    │
└─────────────────────────────────────────────────┘
```

## Data Flow

1. **Market Feeds** → Aggregated price & volume data
2. **Pattern Engine** → Detects opportunities
3. **Signal Broadcast** → Sends to Momentum/Swing via 0G DA
4. **Agent Confirmation** → Trading agents confirm & execute
5. **Reputation Update** → Scout reputation adjusted

## Success Metrics

| Metric | Target |
|--------|--------|
| Signal accuracy | >70% confirmation rate |
| False positive rate | <15% |
| Detection latency | <500ms |
| Uptime | 99.9% |

---

*Part of ColonAI ecosystem for 0G APAC Hackathon*
