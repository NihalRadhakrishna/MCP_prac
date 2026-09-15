"""Deterministic-enough mock prices so trading works without a market-data API key."""

from __future__ import annotations

import random

BASE_PRICES = {
    "AAPL": 190.0,
    "AMZN": 185.0,
    "GOOG": 175.0,
    "GOOGL": 175.0,
    "META": 510.0,
    "MSFT": 420.0,
    "NVDA": 120.0,
    "TSLA": 250.0,
}

_last_price: dict[str, float] = {}


def simulated_price(symbol: str) -> float:
    """Return a slightly jittered price for a symbol."""
    ticker = symbol.upper()
    last = _last_price.get(ticker, BASE_PRICES.get(ticker, 100.0))
    last = max(1.0, last * (1 + random.uniform(-0.01, 0.01)))
    _last_price[ticker] = last
    return round(last, 2)
