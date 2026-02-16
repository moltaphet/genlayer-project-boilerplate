from genlayer import *

@gl_contract
class AIJudge:
    def __init__(self):
       
        self.admin = gl.message.sender

    @gl_external
    def resolve_dispute(self, party_a_statement: str, party_b_statement: str):
       
        prompt = f"""
        Analyze the following dispute and decide who is right. 
        Party A says: {party_a_statement}
        Party B says: {party_b_statement}
        Return only 'A' or 'B' as the winner.
        """
        
        result = gl.nondet.render(prompt)
        return result