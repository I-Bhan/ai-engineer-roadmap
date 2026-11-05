
text4= """
    THIS   IS    A   CONTRACT.

    BETWEEN    TWO   PARTIES.

    The FIRST party agrees to PAY   5000 SAR.

    This contract is VALID.
"""
f="".join(text4.lower().split("\n")).strip()
replace_contract=f.replace("contract","agreement")
count_words=len(replace_contract.split())
count_party=replace_contract.count("party")
print(replace_contract)
print(count_words)
print(count_party)