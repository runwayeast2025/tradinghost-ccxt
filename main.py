import json
import signal
import time

ENGINE = "CCXT"
NEXT_STEPS = [
    "1. Open this repository in Cursor (or your preferred AI coding tool)",
    '2. Tell the AI what to build — e.g. "Build me a grid trading bot for Binance BTC/USDT"',
    "3. The AI will write your strategy using the rules in .cursor/rules/",
    "4. Push to GitHub — TradingHost syncs and restarts automatically",
]

running = True


def log(level, msg, **kwargs):
    print(json.dumps({"level": level, "msg": msg, **kwargs}), flush=True)


def shutdown(sig, frame):
    global running
    running = False


signal.signal(signal.SIGTERM, shutdown)
signal.signal(signal.SIGINT, shutdown)

log("info", "Strategy deployed successfully")
log("info", f"Template: TradingHost + {ENGINE}")
log("info", "")
log("info", "Next steps:")
for step in NEXT_STEPS:
    log("info", f"  {step}")
log("info", "")
log("info", "This placeholder will be replaced when you push your strategy code.")

while running:
    time.sleep(60)
    log("info", "Waiting for strategy code...", hint="Push code to your repository to get started")

log("info", "Shutting down")
