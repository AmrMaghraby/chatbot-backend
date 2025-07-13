def transfer_money(amount: str, recipient: str):
    """Transfer money to another user."""
    return f"✅ Transferred {amount} to {recipient}."

def add_beneficiary(name: str, iban: str):
    """Add a new beneficiary to your account."""
    return f"✅ Added {name} with IBAN {iban} as a beneficiary."

TOOL_FUNCTIONS = {
    "transfer_money": transfer_money,
    "add_beneficiary": add_beneficiary,
}
