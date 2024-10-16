# Functional Test Case Suite: ChainPortX & CCTP Protocols with Thresholds
## Context:
- **Protocols:** ChainPortX and CCTP
- **Chains:** Ethereum, Avalanche, Optimism
- **Threshold logic:** When the ported amount is below or above a defined threshold range, the CCTP protocol is used. When within the threshold range, ChainPortX may be used depending on the chain.
- **Chains Protocol Support:** 
  - **Ethereum:** Supports both ChainPortX & CCTP.
  - **Avalanche:** Supports CCTP only.
  - **Optimism:** Supports both ChainPortX & CCTP.

## Test Case 1: Protocol Selection for Amount Below Threshold (Ethereum)
**Objective:** ChainPortX is not available for amounts below the threshold
- **Preconditions:** User is connected with a MetaMask wallet and selects Ethereum as the chain.
- **Steps:**
1. Attempt to port an amount below the threshold.
2. Observe which protocol is automatically selected.
- **Expected Result:** The CCTP protocol should be selected, and a message should indicate that ChainPortX is not available for amounts below the threshold.

## Test Case 2: Protocol Selection for Amount Above Threshold (Ethereum)
**Objective:** CCTP protocol selected automatically
- **Preconditions:** User is connected with a MetaMask wallet and selects Ethereum as the chain.
- **Steps:**
1. Attempt to port an amount above the threshold.
2. Attempt to port an amount above the threshold.
- **Expected Result:** The CCTP protocol should be selected automatically for amounts above the threshold. The user should be notified that ChainPortX is unavailable for larger amounts.

## Test Case 3: Protocol Selection for Amount Within Threshold (Ethereum)
**Objective:** ChainPortX should be selected for transactions
- **Preconditions:** User is connected with a MetaMask wallet and selects Ethereum as the chain.
- **Steps:**
1. Attempt to port an amount within the threshold range.
2. Observe the protocol selection.
- **Expected Result:** ChainPortX should be selected for transactions within the threshold range. The fee should be calculated based on ChainPortX’s fee structure.

## Test Case 4: Protocol Selection for Amount Below Threshold (Avalanche)
**Objective:** Avalanche should be selected for all amounts
- **Preconditions:** User is connected with a MetaMask wallet and selects Avalanche as the chain.
- **Steps:**
1. Attempt to port an amount below the threshold.
2. Observe the protocol selection.
- **Expected Result:** Since Avalanche only supports CCTP, this protocol should be selected for all amounts, regardless of whether they are below or above the threshold.

## Test Case 5: Protocol Selection for Amount Above Threshold (Avalanche)
**Objective:** CCTP automatically selected
- **Preconditions:** User is connected with a MetaMask wallet and selects Avalanche as the chain.
- **Steps:**
1. Attempt to port an amount above the threshold.
2. Observe the protocol selection.
- **Expected Result:** CCTP should be automatically selected, as it is the only supported protocol on Avalanche. The amount above the threshold should not cause a protocol switch.

## Test Case 6: Protocol Selection for Amount Below Threshold (Optimism)
**Objective:** CCTP automatically selected
- **Preconditions:** User is connected with a MetaMask wallet and selects Optimism as the chain.
- **Steps:**
1. Attempt to port an amount below the threshold.
2. Observe the protocol selection.
- **Expected Result:** CCTP should be selected automatically for amounts below the threshold.

## Test Case 7: Protocol Selection for Amount Above Threshold (Optimism)
**Objective:** CCTP automatically selected
- **Preconditions:** User is connected with a MetaMask wallet and selects Optimism as the chain.
- **Steps:**
1. Attempt to port an amount above the threshold.
2. Observe the protocol selection.
- **Expected Result:** CCTP should be selected automatically for amounts above the threshold.

## Test Case 8: Protocol Selection for Amount Within Threshold (Optimism)
**Objective:** ChainPortX selected
- **Preconditions:** User is connected with a MetaMask wallet and selects Optimism as the chain.
- **Steps:**
1. Attempt to port an amount within the threshold range.
2. Observe the protocol selection.
- **Expected Result:** ChainPortX should be selected for transactions within the threshold range on Optimism, and the fee should be calculated according to ChainPortX’s fee structure.

## Test Case 9: Fee Validation for ChainPortX on Ethereum
**Objective:** Fee for ChainPortX correctly applied
- **Preconditions:** User is connected with a MetaMask wallet and selects Ethereum as the chain with an amount within the threshold range.
- **Steps:**
1. Port the amount within the threshold and verify the fee applied.
- **Expected Result:** The fee for ChainPortX should be correctly applied based on its fee structure. Verify the fee against known values.

## Test Case 10: Fee Validation for CCTP on Ethereum
**Objective:** CCTP applies the correct fee
- **Preconditions:** User is connected with a MetaMask wallet and selects Ethereum as the chain with an amount below or above the threshold.
- **Steps:**
1. Port an amount below or above the threshold and verify the fee applied.
- **Expected Result:** The CCTP protocol should apply the correct fee structure for the transaction.

## Test Case 11: Fee Validation for CCTP on Avalanche
**Objective:** CCTP applies the correct fee regardless of the ported amount
- **Preconditions:** User is connected with a MetaMask wallet and selects Avalanche as the chain
- **Steps:**
1. Port any amount and verify the fee applied.
- **Expected Result:** CCTP fees should be applied correctly for all transactions on Avalanche, regardless of the ported amount.

## Test Case 12: Fee Validation for ChainPortX on Optimism
**Objective:** ChainPortX should apply its fee
- **Preconditions:** User is connected with a MetaMask wallet and selects Optimism as the chain with an amount within the threshold range.
- **Steps:**
1. Port the amount within the threshold and verify the fee applied.
- **Expected Result:** ChainPortX should apply its fee structure, and the fee should be validated against known values.
