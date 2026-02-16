# ⚖️ AI Judge dApp on GenLayer

## Overview
This is a decentralized dispute resolution system. It uses GenLayer's AI-consensus to judge cases between two parties based on their statements and a prior agreement.

## How it Works
1. **Submit Evidence:** Both parties provide their statements.
2. **AI Consensus:** GenLayer validators run the AI model to analyze the case.
3. **Verdict:** A final, tamper-proof decision is reached through network agreement.

## How to Run
1. Start your local node: `docker compose up`
2. Deploy `contracts/ai_judge.py` using GenLayer Studio.
3. Call `evaluate_case` with your test data!