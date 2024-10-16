# Manual Test Cases for Transaction History Tab

## Test Case 1: Display of Transaction History Table with Correct Data Reflection

**Objective:** Ensure that UI accurately reflects the backend data
- **Preconditions:** User is connected with a MetaMask wallet.
- **Steps:**
1. Open the ChainPort app and navigate to the "Transaction History" tab.
2. Use API calls to retrieve transaction history directly from the backend.
3. Compare the transaction data displayed on the UI with the data from the API (i.e., check for all rows, fields like date, token, from/to, etc.).
- **Expected Result:** The UI should accurately reflect the backend data. Differences in token amounts, dates, or blockchain names must be logged with specific error messages.

## Test Case 2: Token Format, Precision, and Icon Validation

**Objective:** Ensure that UI accurately reflects token format, precision and icons
- **Preconditions:** User is connected with a MetaMask wallet.
- **Steps:**
1. Verify that each row displays the correct token name, amount, and the associated icon.
2. Ensure token amounts display appropriate precision (e.g., 2 decimal places for most tokens).
3. Inject large token amounts with many decimal places to test how the UI handles rounding or truncation.
- **Expected Result:** Token names, amounts, and icons should match the backend data. Excessive decimal points should be rounded appropriately, and any discrepancy should trigger an error or warning.

## Test Case 3: Validation of "From" and "To" Blockchain Chains

**Objective:** Labels should be displayed accurately
- **Preconditions:** User is connected with a MetaMask wallet.
- **Steps:**
1. Verify that the "From" and "To" fields show the correct blockchain names (e.g., Polygon -> Ethereum).
2. Simulate incorrect blockchain names in backend data to observe how the UI reacts.
- **Expected Result:** Blockchain labels should be displayed accurately. Invalid or malformed labels should be caught and either flagged in the UI or in logs.

## Test Case 4: Date Format and Sorting Verification
**Objective:** The date follow correct format, sorting working consistently
- **Preconditions:** User is connected with a MetaMask wallet.
- **Steps:**
1. Verify the date format in the "Date" column.
2. Test sorting by ascending and descending date order.
- **Expected Result:** The date should follow the format "Month Day, Year" (e.g., "September 21, 2023"). Sorting should work consistently across different date ranges.

## Test Case 5: Port Fee Display and Calculation
**Objective:** Port fee displayed correctly
- **Preconditions:** User is connected with a MetaMask wallet.
- **Steps:**
1. Verify the "Port Fee" column displays the correct fee for each transaction or shows "N/A" where no fee is applicable.
2. Test various scenarios where port fees are dynamically calculated, including fee-free ports.
- **Expected Result:** Port fee should be displayed correctly, with "N/A" in cases where fees are not applicable.

## Test Case 6: Negative Test - Handling No Transaction History
**Objective:** UI should display a message like "No transactions available"
- **Preconditions:** User is connected with a MetaMask wallet.
- **Steps:**
1. Simulate an account with no transactions.
2. Verify how the "Transaction History" tab behaves when there is no data.
- **Expected Result:** The UI should display a message like "No transactions available" and no empty rows or broken UI elements should appear.

## Test Case 7: Negative Test - Disconnected Wallet Handling
**Objective:** UI should notify the user of the disconnection
- **Preconditions:** User is connected with a MetaMask wallet.
- **Steps:**
1. Disconnect the MetaMask wallet while viewing the "Transaction History" tab.
2. Refresh the page and try to access the history.
- **Expected Result:** The UI should notify the user of the disconnection, and transaction history should not be displayed without an active wallet connection.

## Test Case 8: Download Transaction History CSV
**Objective:** The CSV file should match the UI data.
- **Preconditions:** User is connected with a MetaMask wallet.
- **Steps:**
1. Click the "Download Tx history CSV" button.
2. Verify that the CSV file downloads correctly and that the data matches what is displayed on the UI.
3. Intentionally corrupt backend data and check the exported CSV for accuracy.
- **Expected Result:** The CSV file should be complete and match the UI data. Any malformed or incorrect entries should be caught and flagged during the export process.

## Test Case 9: Negative Test - API Timeout or Backend Unavailability
**Objective:** UI should display a timeout or network error message
- **Preconditions:** User is connected with a MetaMask wallet.
- **Steps:**
1. Simulate an API timeout or backend unavailability when fetching transaction history.
2. Attempt to load the "Transaction History" tab during this downtime.
- **Expected Result:** The UI should display a timeout or network error message and prompt the user to retry. No stale data should be displayed in case of an API failure.

## Test Case 10: Responsive Design and Layout for Mobile Devices
**Objective:** Table should be fully responsive
- **Preconditions:** User is connected with a MetaMask wallet.
- **Steps:**
1. Open the ChainPort app on different screen sizes (desktop, tablet, mobile).
2. Verify that the transaction history table adjusts properly on smaller screens.
- **Expected Result:** The table should be fully responsive, with no broken layouts. Columns should adjust dynamically, and horizontal scrolling should work smoothly on smaller devices.

## Test Case 11: Validation of Large Transaction Volumes
**Objective:** UI handles large numbers gracefully
- **Preconditions:** User is connected with a MetaMask wallet.
- **Steps:**
1. Simulate a large transaction volume (e.g., over 10,000 tokens).
2. Verify that the UI handles large numbers appropriately, including correct formatting (e.g., 10,000+ tokens with proper commas).
- **Expected Result:** The UI should handle large numbers gracefully, ensuring that the format does not overflow or break the layout.

## Test Case 12: Security Test - Unauthorized Access Prevention
**Objective:** Unauthorized access should be blocked
- **Preconditions:** User is connected with a MetaMask wallet.
- **Steps:**
1. Simulate an unauthorized user trying to access the "Transaction History" tab without connecting their wallet.
2. Test session hijacking or invalid access token scenarios.
- **Expected Result:** Unauthorized access should be blocked, and the user should be redirected to a wallet connection prompt. All transactions should be securely fetched and displayed only when a valid wallet connection is active.

## Test Case 13: Pagination and Scrolling for Large Data Sets
**Objective:** Pagination or infinite scrolling should function smoothly
- **Preconditions:** User is connected with a MetaMask wallet.
- **Steps:**
1. Simulate a large transaction history (100+ transactions).
2. Verify that pagination or infinite scrolling is implemented correctly, allowing access to all transaction history.
- **Expected Result:** Pagination or infinite scrolling should function smoothly, without performance degradation. Users should be able to load additional transactions seamlessly.

## Test Case 14: UI State After Page Refresh
**Objective:** After refreshing the transaction history should maintain its state
- **Preconditions:** User is connected with a MetaMask wallet.
- **Steps:**
1. Refresh the "Transaction History" tab while the data is loaded.
2. Verify if the UI state (sorted order, filters applied) is preserved post-refresh.
- **Expected Result:** After refreshing, the transaction history should maintain its state (sort order, filters), and all data should be correctly reloaded without duplication or errors.
