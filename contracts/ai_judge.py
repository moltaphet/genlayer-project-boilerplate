# v0.1.0
# { "Depends": "py-genlayer:latest" }

from genlayer import *
import json
import typing

class AIJudge(gl.Contract):
    is_resolved: bool
    agreement_terms: str
    evidence_url: str
    verdict: str

    def __init__(self, agreement_terms: str, evidence_url: str):
        """
        Initializes the arbitration case.
        """
        self.is_resolved = False
        self.agreement_terms = agreement_terms
        self.evidence_url = evidence_url
        self.verdict = "PENDING"

    @gl.public.write
    def resolve_dispute(self) -> typing.Any:
        if self.is_resolved:
            return "Judgment already finalized"

        evidence_url = self.evidence_url
        terms = self.agreement_terms

        def get_ai_judgment() -> typing.Any:
            # Fetch evidence data from the web
            web_data = gl.nondet.web.render(evidence_url, mode="text")
            
            task = f"""
            Act as a digital judge. 
            Contract Terms: {terms}
            Evidence from Web: {web_data}

            Compare the evidence against the terms.
            If the terms are met, Winner is 1 (Claimant).
            If the terms are violated, Winner is 2 (Defendant).

            Respond ONLY in JSON:
            {{
                "winner": int, 
                "reason": "short explanation"
            }}
            """
            # Execute AI prompt and clean JSON formatting
            result = (
                gl.nondet.exec_prompt(task).replace("```json", "").replace("```", "")
            )
            return json.loads(result)

        # Consensus mechanism
        result_json = gl.eq_principle.strict_eq(get_ai_judgment)

        # Record result on-chain
        if result_json["winner"] > 0:
            self.is_resolved = True
            if result_json["winner"] == 1:
                self.verdict = f"WINNER: CLAIMANT - {result_json['reason']}"
            else:
                self.verdict = f"WINNER: DEFENDANT - {result_json['reason']}"

        return result_json

    @gl.public.view
    def get_status(self) -> dict[str, typing.Any]:
        return {
            "verdict": self.verdict,
            "resolved": self.is_resolved,
            "terms": self.agreement_terms
        }