# Reimbursement Calculator

This project calculates reimbursement amounts for a set of projects based on specific rules regarding travel days, full days, and city types (high-cost vs. low-cost).

## Prerequisites

- Python 3.7 or later

## How to Run

1. Ensure you have Python 3.7 or later installed on your system.
2. Save the `reimbursement_calculator.py` file to your local machine.
3. Open a terminal or command prompt.
4. Navigate to the directory containing the `reimbursement_calculator.py` file.
5. Run the following command:

   ```
   python reimbursement_calculator.py
   ```

## Expected Output

The script will process four predefined scenarios and output the results. For each scenario, you will see:

1. The set number
2. Details of each project in the set
3. The calculated reimbursement for the set

The output will be in the following format:

```
Set 1:
  Project 1: [City Type], Start Date: [MM/DD/YY], End Date: [MM/DD/YY]
  Reimbursement: $[Amount]

Set 2:
  Project 1: [City Type], Start Date: [MM/DD/YY], End Date: [MM/DD/YY]
  Project 2: [City Type], Start Date: [MM/DD/YY], End Date: [MM/DD/YY]
  ...
  Reimbursement: $[Amount]

...
```

## Example Output

```
Set 1:
  Project 1: Low Cost City, Start Date: 09/01/15, End Date: 09/03/15
  Reimbursement: $165

Set 2:
  Project 1: Low Cost City, Start Date: 09/01/15, End Date: 09/01/15
  Project 2: High Cost City, Start Date: 09/02/15, End Date: 09/06/15
  Project 3: Low Cost City, Start Date: 09/06/15, End Date: 09/08/15
  Reimbursement: $590

Set 3:
  Project 1: Low Cost City, Start Date: 09/01/15, End Date: 09/03/15
  Project 2: High Cost City, Start Date: 09/05/15, End Date: 09/07/15
  Project 3: High Cost City, Start Date: 09/08/15, End Date: 09/08/15
  Reimbursement: $445

Set 4:
  Project 1: Low Cost City, Start Date: 09/01/15, End Date: 09/01/15
  Project 2: Low Cost City, Start Date: 09/01/15, End Date: 09/01/15
  Project 3: High Cost City, Start Date: 09/02/15, End Date: 09/02/15
  Project 4: High Cost City, Start Date: 09/02/15, End Date: 09/03/15
  Reimbursement: $185
```