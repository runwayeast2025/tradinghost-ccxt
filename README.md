# TradingHost + CCXT

Build and deploy trading bots for 100+ crypto exchanges using [CCXT](https://github.com/ccxt/ccxt) on [TradingHost](https://tradinghost.com).

## What is this?

This repository is an AI-powered development scaffold. Use it as a template (click "Use this template" on GitHub), open your new repo in your AI coding tool (Cursor, Claude, Codex), and tell the AI what you want to build. The rules in `.cursor/rules/` teach the AI everything it needs to know about CCXT and TradingHost to help you create a production-quality trading bot.

## Getting Started

1. **Click "Use this template"** → Create a new repository (you can make it private)
2. **Open in Cursor** (or your preferred AI coding tool)
3. **Tell the AI what to build** — e.g. "Build me a grid trading bot for Binance BTC/USDT"
4. **Set credentials** — add your exchange API key/secret as TradingHost strategy secrets (`EXCHANGE_API_KEY`, `EXCHANGE_API_SECRET`); edit non-secret tunables (exchange, symbols, testnet) in `config.json`. Secrets are environment variables, never committed to git.
5. **Deploy on TradingHost** — link this repo as a strategy, create a deployment, and you're live

## Supported Exchanges

CCXT supports 100+ exchanges including: Binance, Bybit, OKX, Kraken, Coinbase, KuCoin, Gate.io, Bitget, MEXC, and many more. Both spot and futures markets are supported.

## TradingHost Deployment

1. Create an account at [tradinghost.com](https://tradinghost.com)
2. Link this GitHub repository as a strategy
3. Create a deployment (choose region: London, New York, or Tokyo)
4. Your bot runs 24/7 with persistent storage, monitoring, and real-time logs

## Documentation

- [TradingHost Docs](https://tradinghost.com/docs)
- [CCXT Documentation](https://docs.ccxt.com)
- [CCXT Exchange List](https://github.com/ccxt/ccxt/wiki/Exchange-Markets)

## Risk Warning

Trading cryptocurrencies involves significant risk of loss. This software is provided as-is with no guarantees. Always test with small amounts or testnet before trading real funds.
