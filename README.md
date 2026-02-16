
```markdown
# ⚖️ AI Judge: Next-Gen Decentralized Arbitration
**An Intelligent Dispute Resolution Protocol built on GenLayer**

---

## 🌟 Overview
Traditional legal disputes are slow, expensive, and centralized. **AI Judge** is a decentralized dApp that leverages GenLayer's unique **AI-Consensus** to provide instant, fair, and tamper-proof verdicts. By connecting directly to web-based evidence, it bridges the gap between real-world data and blockchain finality.

## 🚀 Key Features
- **🌐 Web-Evidence Integration:** Automatically fetches real-time data from any URL using `gl.nondet.web.render`.
- **🤖 Deterministic AI Logic:** Uses GenLayer's `strict_eq` consensus to ensure all validators agree on the AI's verdict.
- **🔐 Immutable Judgments:** Once a case is "FINALIZED", the verdict and reasoning are permanently etched onto the blockchain.
- **⚡ Zero-Trust Arbitration:** No human middleman; the code and the AI model are the judge and jury.

---

## 🏗 Architecture & Flow
The contract follows a sophisticated non-deterministic flow to ensure accuracy:

1. **Initialization:** Parties define the `agreement_terms` and provide an `evidence_url`.
2. **Consensus Trigger:** The `resolve_dispute` function is called.
3. **Off-Chain Execution:** Validators fetch web data and run the LLM prompt.
4. **Validation:** The `strict_eq` principle ensures every node reaches the exact same JSON output.
5. **Finalization:** The state is updated, and the winner is declared.



---

## 💻 Technical Implementation
The contract is written in Python using the latest `py-genlayer:latest` framework.

### Example Input:
- **Agreement Terms:** `"Seller must provide proof of delivery for the digital asset by Feb 2026."`
- **Evidence URL:** `"https://api.github.com/repos/moltaphet/project/releases"`

### Success Result (Finalized):
```json
{
  "winner": 1,
  "reason": "The release log on GitHub confirms the asset was delivered on schedule.",
  "status": "FINALIZED"
}

```

---

## 🛠 Installation & Testing

To run this project locally, follow these steps:

1. **Clone the repository:**
```bash
git clone [https://github.com/moltaphet/genlayer-project-boilerplate.git](https://github.com/moltaphet/genlayer-project-boilerplate.git)
cd genlayer-project-boilerplate

```


2. **Spin up the GenLayer Node:**
Make sure Docker is running, then execute:
```bash
docker compose up

```


3. **Deploy the Contract:**
* Open [GenLayer Studio](https://studio.genlayer.com/).
* Upload `contracts/ai_judge.py`.
* Click **Deploy** and interact with the functions!



---

## 📝 Mission Submission

This project is part of the **"From Zero to GenLayer"** mission. It demonstrates the power of AI-driven smart contracts in solving complex, real-world problems through decentralized consensus.

**Developed by:** [Moltaphet]
**Powered by:** GenLayer AI Consensus

```