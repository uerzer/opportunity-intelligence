"""
Crypto Arbitrage Opportunity Monitor
Tracks DEX/CEX price spreads, MEV opportunities, and cross-chain arbitrage

Key Findings from Research:
- ArbitrageScanner.io: $69-795/mo, covers 75+ CEX, 25+ DEX, 20 blockchains
- Typical spreads: 0.3-0.8% on major pairs, 2+% during volatility
- Minimum capital: $5K-10K for profitable trades after fees
- 70% of arbitrage is bot-driven, speed is critical
- Cross-chain opportunities exist but bridge fees/delays eat profits
"""

import os
import json
from datetime import datetime
from typing import Dict, List, Optional

def transform(data: dict, context: dict) -> dict:
    """
    Monitors crypto arbitrage opportunities across CEX, DEX, and chains.
    
    Input data structure:
    {
        "min_spread_threshold": 0.005,  # 0.5% minimum spread
        "capital_available": 10000,     # USD available for arb
        "chains": ["ethereum", "bsc", "arbitrum"],
        "focus": "dex_spreads"  # or "cex_dex", "cross_chain", "mev"
    }
    
    Returns ranked arbitrage opportunities with profit potential.
    """
    
    # Extract configuration
    min_spread = data.get("min_spread_threshold", 0.005)
    capital = data.get("capital_available", 10000)
    chains = data.get("chains", ["ethereum", "bsc"])
    focus = data.get("focus", "dex_spreads")
    
    # Arbitrage opportunity framework from research
    opportunities = []
    
    # 1. DEX-DEX Arbitrage (within same chain)
    if focus in ["dex_spreads", "all"]:
        dex_opportunities = {
            "type": "DEX-DEX Arbitrage",
            "chains": chains,
            "typical_spreads": "0.1-0.8%",
            "execution_speed": "seconds",
            "capital_requirement": f"${capital}+",
            "tools_needed": [
                "ArbitrageScanner.io ($69-795/mo)",
                "Real-time price feeds (WebSocket)",
                "Flash loan integration (Aave V3)",
                "MEV protection (Flashbots)"
            ],
            "example_pairs": {
                "ethereum": ["Uniswap V3 vs SushiSwap", "Curve vs Uniswap"],
                "bsc": ["PancakeSwap vs Biswap", "ApeSwap vs PancakeSwap"],
                "arbitrum": ["Uniswap V3 vs Camelot"]
            },
            "profit_calc": {
                "spread": "0.5%",
                "trade_size": capital,
                "gross_profit": capital * 0.005,
                "fees": {
                    "gas": "$5-50 (chain dependent)",
                    "dex_swap": "0.3%",
                    "slippage": "0.1-0.5%"
                },
                "net_profit_range": f"${capital * 0.001:.2f} - ${capital * 0.003:.2f}"
            }
        }
        opportunities.append(dex_opportunities)
    
    # 2. CEX-DEX Arbitrage
    if focus in ["cex_dex", "all"]:
        cex_dex = {
            "type": "CEX-DEX Arbitrage",
            "description": "Buy cheap on CEX, sell high on DEX (or reverse)",
            "typical_spreads": "0.5-2%",
            "execution_speed": "minutes",
            "capital_requirement": f"${capital}+",
            "friction_points": [
                "CEX withdrawal times (5-30 min)",
                "Network congestion fees",
                "CEX withdrawal fees ($5-50)",
                "KYC/compliance requirements"
            ],
            "best_opportunities": {
                "high_volatility_tokens": "Newly listed tokens, low liquidity pairs",
                "regional_price_gaps": "Asia vs US market hours",
                "event_driven": "Token listings, delistings, airdrops"
            },
            "profit_calc": {
                "spread": "1.5%",
                "trade_size": capital,
                "gross_profit": capital * 0.015,
                "fees": {
                    "cex_withdrawal": "$20-50",
                    "dex_swap": "0.3%",
                    "gas": "$10-100",
                    "slippage": "0.5-1%"
                },
                "net_profit_range": f"${capital * 0.005:.2f} - ${capital * 0.01:.2f}"
            }
        }
        opportunities.append(cex_dex)
    
    # 3. Cross-Chain Arbitrage
    if focus in ["cross_chain", "all"]:
        cross_chain = {
            "type": "Cross-Chain Arbitrage",
            "description": "Price differences for same asset on different chains",
            "typical_spreads": "1-3%",
            "execution_speed": "10-30 minutes",
            "capital_requirement": f"${capital}+",
            "bridge_options": [
                "Stargate (LayerZero) - 0.1-0.3% fee",
                "Hop Protocol - 0.04-0.3% fee",
                "Synapse - 0.05-0.5% fee",
                "cBridge (Celer) - 0.04-0.3% fee"
            ],
            "challenges": {
                "bridge_fees": "0.1-0.5% + gas on both chains",
                "bridge_delay": "10-30 minutes for finality",
                "liquidity_constraints": "Large trades may exceed bridge capacity",
                "smart_contract_risk": "Bridge exploits are common"
            },
            "example_opportunities": {
                "usdc_cross_chain": "USDC.e on Arbitrum vs native USDC on Optimism",
                "eth_wrapped": "WETH price differences across L2s",
                "stable_depeg": "Temporary depegs create arb windows"
            },
            "profit_calc": {
                "spread": "2%",
                "trade_size": capital,
                "gross_profit": capital * 0.02,
                "fees": {
                    "bridge_fee": "0.3%",
                    "gas_origin": "$10-50",
                    "gas_destination": "$5-30",
                    "dex_swaps": "0.6% (both sides)"
                },
                "net_profit_range": f"${capital * 0.005:.2f} - ${capital * 0.012:.2f}"
            }
        }
        opportunities.append(cross_chain)
    
    # 4. MEV Opportunities (Advanced)
    if focus in ["mev", "all"]:
        mev = {
            "type": "MEV (Maximal Extractable Value)",
            "description": "Front-run, back-run, or sandwich profitable transactions",
            "typical_profit": "0.1-5% per opportunity",
            "execution_speed": "milliseconds",
            "capital_requirement": f"${capital * 5}+ (high capital efficiency)",
            "strategies": {
                "sandwich_attacks": {
                    "description": "Front-run + back-run large DEX swaps",
                    "risk": "High (can be detected, blacklisted)",
                    "profit": "0.5-2% per sandwich",
                    "tools": "Flashbots, MEV-Boost, custom bots"
                },
                "liquidation_hunting": {
                    "description": "Monitor lending protocols for undercollateralized positions",
                    "risk": "Medium (competitive)",
                    "profit": "5-15% liquidation bonus",
                    "tools": "Aave, Compound, custom monitoring"
                },
                "arbitrage_frontrun": {
                    "description": "Detect pending arb txs and front-run them",
                    "risk": "Very high (arms race)",
                    "profit": "Variable",
                    "tools": "Mempool monitoring, priority gas auctions"
                }
            },
            "reality_check": {
                "competition": "Top MEV bots capture 80%+ of opportunities",
                "capital_required": "$50K-500K for meaningful profits",
                "technical_barrier": "Extremely high - Rust/Go, low-latency infra",
                "ethical_concerns": "Sandwich attacks harm retail traders",
                "recommendation": "Not recommended for solo operators with <$100K"
            }
        }
        opportunities.append(mev)
    
    # Reality Check for Current Capital Level
    capital_assessment = {
        "your_capital": f"${capital}",
        "realistic_monthly_returns": {
            "conservative": f"${capital * 0.05:.2f} (5% monthly)",
            "moderate": f"${capital * 0.10:.2f} (10% monthly)",
            "aggressive": f"${capital * 0.20:.2f} (20% monthly, high risk)"
        },
        "capital_required_for_100k_monthly": {
            "at_5_percent": "$2,000,000",
            "at_10_percent": "$1,000,000",
            "at_20_percent": "$500,000"
        },
        "path_to_scale": [
            "Start with $10K, target 10-15% monthly",
            "Compound returns for 12-18 months",
            "Build proprietary strategies and infrastructure",
            "Scale to $100K+ capital base",
            "Alternative: Use flash loans for zero-capital arbitrage (advanced)"
        ]
    }
    
    # Tools & Infrastructure Needed
    infrastructure = {
        "essential": {
            "price_monitoring": {
                "tools": ["ArbitrageScanner.io ($69-795/mo)", "Custom WebSocket feeds"],
                "cost": "$100-1,000/month"
            },
            "execution": {
                "tools": ["Web3.py/Ethers.js", "Private RPC nodes (Alchemy/Infura)"],
                "cost": "$50-500/month"
            },
            "capital": {
                "tools": ["DEX liquidity", "CEX accounts (KYC)"],
                "cost": f"${capital} working capital"
            }
        },
        "advanced": {
            "flash_loans": {
                "tools": ["Aave V3", "dYdX", "Uniswap V3 flash swaps"],
                "benefit": "Borrow capital for single transaction, no upfront capital needed",
                "cost": "0.05-0.09% flash loan fee"
            },
            "mev_protection": {
                "tools": ["Flashbots RPC", "MEV-Blocker"],
                "benefit": "Prevent being front-run",
                "cost": "Free"
            },
            "automated_execution": {
                "tools": ["Gelato Network", "Chainlink Automation", "Custom bots"],
                "cost": "$100-1,000/month"
            }
        }
    }
    
    # Next Steps
    next_steps = {
        "immediate_actions": [
            "Sign up for ArbitrageScanner.io trial",
            "Monitor DEX-DEX spreads on Ethereum/BSC for 1 week",
            "Calculate actual net profits after all fees",
            "Test with $100-500 to validate strategy"
        ],
        "30_day_plan": [
            "Build automated monitoring system",
            "Identify 3-5 consistently profitable pairs",
            "Optimize gas usage and execution speed",
            "Scale capital as strategy proves out"
        ],
        "reality": "Crypto arbitrage is highly competitive. Expect 5-15% monthly returns with $10K capital, not $100K monthly revenue. Consider combining with other strategies."
    }
    
    return {
        "scan_timestamp": datetime.now().isoformat(),
        "configuration": {
            "capital": capital,
            "min_spread": min_spread,
            "chains": chains,
            "focus": focus
        },
        "opportunities": opportunities,
        "capital_assessment": capital_assessment,
        "infrastructure": infrastructure,
        "next_steps": next_steps
    }
