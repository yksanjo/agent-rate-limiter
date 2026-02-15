#!/usr/bin/env python3
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src import AgentRateLimiter
def main():
    print("Agent Rate Limiter Demo")
    r = AgentRateLimiter(max_requests=2)
    print(f"Allowed 1: {r.allow('a1')}")
    print(f"Allowed 2: {r.allow('a1')}")
    print(f"Allowed 3: {r.allow('a1')}")
    print("Done!")
if __name__ == "__main__": main()
