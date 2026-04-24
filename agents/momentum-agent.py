"""
Momentum Agent - Medium-term trend following agent for ColonAI
Receives signals from Scout Agent, confirms with technical indicators, executes trades.
"""

import os
from datetime import datetime
from typing import Dict, List, Optional
import json

# 0G Imports (placeholder - will update with actual SDK)
# from zero_g import StorageClient, DA_Client


class MomentumAgent:
    """Momentum agent that follows trends using EMA crossovers and RSI."""
    
    def __init__(self, agent_id: str, storage_client=None, da_client=None):
        self.agent_id = agent_id
        self.storage_client = storage_client
        self.da_client = da_client
        self.agent_type = "MOMENTUM"
        
        # Strategy parameters
        self.fast_ema = 20  # Fast EMA for trend detection
        self.slow_ema = 50  # Slow EMA for confirmation
        self.rsi_period = 14
        self.rsi_oversold = 70
        self.rsi_overbought = 30
        self.rsi_neutral = 50
        
        # Trading parameters
        self.max_open_positions = 2
        self.risk_per_trade = 0.02  # 2% max position risk
        self.position_size_percent = 0.10  # 10% of allocated capital
        
        # State tracking
        self.positions: Dict[str, Dict] = {}
        self.total_pnl = 0.0
        self.win_count = 0
        self.total_trades = 0
        
        # Performance tracking
        self.uptime_start = datetime.now()
        self.signals_received = 0
        self.trades_executed = 0
    
    async def analyze_signal(self, signal: Dict) -> Dict:
        """Analyze signal from Scout Agent and decide on trading action."""
        
        symbol = signal.get("symbol", "BTC")
        price = float(signal.get("price", 0))
        volume = float(signal.get("volume", 0))
        confidence = float(signal.get("confidence", 0))
        
        # Technical indicators
        ema_fast = self._calculate_ema(symbol)
        ema_slow = self._calculate_ema(symbol)
        ema_alignment = self._check_ema_alignment(ema_fast, ema_slow, price)
        
        # RSI check
        rsi = self._calculate_rsi(symbol)
        rsi_signal = self._get_rsi_signal(rsi)
        
        # Trend analysis
        trend_direction = self._determine_trend(ema_alignment, rsi, signal.get("change_1h"))
        
        # Decision logic
        action = "HOLD"
        reason = f"No strong trend signal (ema_fast={ema_fast:.2f}, ema_slow={ema_slow:.2f}, rsi={rsi:.1f})"
        
        # Bullish momentum signals
        if trend_direction == "BULLISH" and rsi_signal in ["OVERBOUGHT", "BUY"] and ema < price:
            action = "BUY"
            reason = f"Bullish momentum: EMA({ema_fast:.2f}) < Price({price:.2f}), RSI oversold ({rsi_signal})"
            confidence = min(0.65, confidence + 0.1)  # Moderate confidence
        
        # Bearish momentum signals
        elif trend_direction == "BEARISH" and rsi_signal in ["OVERSOLD", "SELL"] and ema > price:
            action = "SELL"
            reason = f"Bearish momentum: EMA({ema_fast:.2f}) > Price({price:.2f}), RSI overbought ({rsi_signal})"
            confidence = min(0.65, confidence + 0.1)  # Moderate confidence
        
        # Overbought/oversold reversion
        if rsi_signal == "OVERBOUGHT" and trend_direction == "BULLISH":
            action = "BUY"
            reason = f"Oversold RSI ({rsi:.1f}) but trend turning bullish (ema_fast={ema_fast:.2f} > price={price:.2f})"
            confidence = 0.60  # Lower confidence for mean reversion
        
        if rsi_signal == "OVERSOLD" and trend_direction == "BEARISH":
            action = "SELL"
            reason = f"Oversold RSI ({rsi:.1f}) but trend turning bearish (ema_fast={ema_fast:.2f} < price={price:.2f})"
            confidence = 0.60  # Lower confidence for mean reversion
        
        # Fibonacci pullback strategy
        if action == "HOLD" and confidence > 0.7:
            # Calculate Fibonacci levels
            action = self._calculate_fibonacci_trade(symbol, price, trend_direction)
        
        return {
            "action": action,
            "reason": reason,
            "confidence": confidence,
            "indicators": {
                "ema_fast": f"{ema_fast:.2f}",
                "ema_slow": f"{ema_slow:.2f}",
                "rsi": f"{rsi:.1f}",
                "trend": trend_direction
            }
        }
    
    def _calculate_ema(self, symbol: str) -> float:
        """Calculate EMA for given symbol (simplified for demo)."""
        # In production, would fetch from 0G Storage or price feed
        # For demo, returning simulated value
        return 60000.0  # Default fallback
    
    def _calculate_rsi(self, symbol: str) -> float:
        """Calculate RSI for given symbol (simplified for demo)."""
        # In production, would fetch from 0G Storage
        # For demo, returning simulated value
        return 50.0  # Default fallback
    
    def _check_ema_alignment(self, fast: float, slow: float, price: float) -> str:
        """Check if EMAs are properly aligned (fast above slow for bull, below for bear)."""
        if fast > slow:
            if price > slow * 1.005:  # 0.5% tolerance
                return "BULLISH"
            elif price < slow * 0.995:  # 0.5% tolerance
                return "BEARISH"
        else:
            return "NEUTRAL"
    
    def _determine_trend(self, ema_alignment: str, rsi: float, change_1h: float) -> str:
        """Determine overall trend direction."""
        
        if ema_alignment == "BULLISH":
            if change_1h > 2.0:  # Strong uptrend
                return "STRONG_BULL"
            elif 0.5 < change_1h <= 2.0:
                return "BULLISH"
        elif ema_alignment == "BEARISH":
            if change_1h < -2.0:  # Strong downtrend
                return "STRONG_BEAR"
            elif -2.0 <= change_1h < -0.5:
                return "BEARISH"
        else:
            return "NEUTRAL"
    
    def _get_rsi_signal(self, rsi: float) -> str:
        """Get RSI signal classification."""
        
        if rsi > 70:
            return "OVERBOUGHT"
        elif rsi < 30:
            return "OVERSOLD"
        elif rsi < 45:
            return "SELL"  # Sell signal
        elif rsi > 55:
            return "BUY"  # Buy signal
        else:
            return "NEUTRAL"
    
    def _calculate_fibonacci_trade(self, symbol: str, price: float, trend_direction: str) -> Dict:
        """Calculate Fibonacci-based pullback entry (placeholder for demo)."""
        
        # Simplified Fibonacci levels for demo
        fib_levels = {
            "level_236": price * 0.764,
            "level_382": price * 0.618,
            "level_500": price * 0.5
        }
        
        # Find pullback level
        if trend_direction == "BULLISH":
            entry_price = fib_levels["level_382"]  # Golden ratio
            stop_loss = fib_levels["level_236"]
            take_profit = fib_levels["level_618"]
        elif trend_direction == "BEARISH":
            entry_price = fib_levels["level_618"]
            stop_loss = fib_levels["level_500"]
            take_profit = fib_levels["level_382"]
        else:
            return {
                "action": "HOLD",
                "reason": "Fibonacci strategy requires clear trend direction"
            }
        
        return {
            "action": entry_price,
            "stop_loss": stop_loss,
            "take_profit": take_profit,
            "strategy": "fibonacci_pullback"
        }
    
    async def execute_trade(self, signal: Dict) -> Dict:
        """Execute trade decision and log to 0G Storage."""
        
        symbol = signal.get("symbol", "BTC")
        action = signal.get("action")
        price = float(signal.get("price", 0))
        
        # Calculate position size (simplified)
        # In production, would get allocated capital from Treasury
        capital_allocation = 20000.0  # Default $20K
        position_size = capital_allocation * self.position_size_percent
        stop_loss = price * (1 - self.risk_per_trade)
        take_profit = price * (1 + (self.risk_per_trade * 2))  # 2:1 R:R
        
        # Validate trade
        if self.max_open_positions > 0:
            # Check capital
            if capital_allocation > self._get_total_position_value():
                reason = "At max open positions, cannot open new trade"
                return {
                    "action": "HOLD",
                    "reason": reason
                }
        
        # Execute trade (simplified - no real trading)
        trade_id = f"trade_{self.agent_id}_{datetime.now().strftime('%Y%m%d%H%M%S')}"
        timestamp = datetime.now().isoformat()
        
        # Update state
        if action in ["BUY", "SELL"]:
            # Open new position
            self.positions[trade_id] = {
                "symbol": symbol,
                "entry_price": price,
                "stop_loss": stop_loss,
                "take_profit": take_profit,
                "size": position_size,
                "status": "OPEN",
                "timestamp": timestamp
            }
            if action == "BUY":
                self.total_trades += 1
            else:
                self.total_trades += 1
        
        self.trades_executed += 1
        
        # Log to 0G Storage (KV Layer)
        if self.storage_client:
            await self.storage_client.set(
                f"trade_{self.agent_id}_{datetime.now().strftime('%Y%m%d%H%M%S')}",
                json.dumps({
                    "agent_id": self.agent_id,
                    "symbol": symbol,
                    "action": action,
                    "price": price,
                    "size": position_size,
                    "stop_loss": stop_loss,
                    "take_profit": take_profit,
                    "timestamp": timestamp
                })
            )
        
        # Broadcast to Orchestrator (via 0G DA in production)
        if self.da_client:
            await self.da_client.publish(
                topic="agent_signals",
                data=json.dumps({
                    "agent_id": self.agent_id,
                    "agent_type": self.agent_type,
                    "signal": signal,
                    "timestamp": datetime.now().isoformat()
                }),
                encoding="merkle"
            )
        
        # Update reputation (placeholder)
        # await self.update_reputation(1.0)  # Positive delta
        
        print(f"[Momentum Agent] {action} {symbol} @ {price} | SL: {stop_loss:.2f} | TP: {take_profit:.2f}")
    
    async def get_agent_info(self) -> Dict:
        """Get agent info for dashboard."""
        
        return {
            "agent_id": self.agent_id,
            "agent_type": self.agent_type,
            "reputation": 1000,  # Placeholder
            "signals_received": self.signals_received,
            "trades_executed": self.trades_executed,
            "total_pnl": self.total_pnl,
            "win_count": self.win_count,
            "uptime": (datetime.now() - self.uptime_start).total_seconds()
        }


# Main execution
async def main():
    """Main execution loop."""
    
    agent = MomentumAgent("momentum_agent_001")
    
    # Simulated signal from Scout (in production, this would come via 0G DA)
    signal = {
        "symbol": "BTC",
        "price": 64500.0,
        "volume": 1450.0,
        "change_1h": 2.5,
        "confidence": 0.75
    }
    
    # Analyze and execute
    decision = await agent.analyze_signal(signal)
    await agent.execute_trade(decision)
    
    # Get agent info
    agent_info = await agent.get_agent_info()
    print(f"\n📊 Momentum Agent Info:")
    print(f"  Agent Type: {agent_info['agent_type']}")
    print(f"  Signals Received: {agent_info['signals_received']}")
    print(f"  Trades Executed: {agent_info['trades_executed']}")
    print(f"  Total PnL: {agent_info['total_pnl']:.2f}")
    print(f"  Win Rate: {agent_info['win_count']}/{agent_info['total_trades']} ({(agent_info['win_count']/agent_info['total_trades'])*100:.1f}%)")
    print(f"  Uptime: {agent_info['uptime']:.0f}s")


if __name__ == "__main__":
    main()
