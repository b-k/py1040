
def get_amt_exemption(income):
    if (status=="single" or status=="head of household") and income < 119200:
        return 53600
    if (status=="married filing jointly") and income < 158900:
        return 83400
    if (status=="married") and income < 79450:
        return 41700
    print("AMT exemption is partially implemented.")
    return 0


def get_tamt(income):
    if income==0: return 0
    if status=="married":
        return income * (.26 if  income <=92700 else .28) - 1854
    else:
        return income * (.26 if  income <=185400 else .28) - 3708

f6251=dict(
amt_div1=cell(0.1, ">>>>>>>>>>>>> AMT income           "),
amt_div2=cell(28.9, ">>>>>>>>>>>>> AMT                  "),
agi_minus_ded=cell(1, "AGI minus deductions", 'CV("agi_minus_deductions")', ('agi_minus_deductions',)),

amt_medical=cell(2, "Medical and dental", 
     "max(min(CV('excess_medical'), .025*CV('agi_again')), 0) if (over_65 or spouse_over_65) else 0",
     ('excess_medical', 'agi_again')),
taxes_deducted=cell(3, "Taxes deducted on Schedule A", "CV('total_taxes_deducted')", ('total_taxes_deducted',)),

mort_interest_adjustment=cell(4, "home mortgage interest adjustment, if any, from line 6 of the worksheet in the instructions for this line 4 (UI)", '0'),

misc_deductions=cell(5, "Miscellaneous deductions from Schedule A",
                "CV('expenses_minus_agi_slice')", ('expenses_minus_agi_slice',)),
amt_deduction_deduction=cell(6, "Reduction for limited deductions (UI)", '0'),
amt_refund_deduction=cell(7, "Tax refund from Form 1040, line 10 or line 21 (only L10 implemented)", 
    "CV('taxable_tax_refunds')", ('taxable_tax_refunds',)),
amt_investment_expense_deduction=cell(8, "Investment interest expense (UI)", '0'),
amt_depletion_deduction=cell(9, "Depletion (UI)", '0'),
nold=cell(10, "NOLD (UI)", '0'),
amt_nold=cell(11, "Alt NOLD (UI)", '0'),
## Got bored. All of these will not be implemented

# 12 Interest from specified private activity bonds exempt from the regular tax . . . . . . . . . . 12
# 13 Qualified small business stock, see instructions . . . . . . . . . . . . . . . . . . . 13
# 14 Exercise of incentive stock options (excess of AMT income over regular tax income) . . . . . . . . 14
# 15 Estates and trusts (amount from Schedule K-1 (Form 1041), box 12, code A) . . . . . . . . . 15
# 16 Electing large partnerships (amount from Schedule K-1 (Form 1065-B), box 6) . . . . . . . . . 16
# 17 Disposition of property (difference between AMT and regular tax gain or loss) . . . . . . . . . 17
# 18 Depreciation on assets placed in service after 1986 (difference between regular tax and AMT) . . . . 18
# 19 Passive activities (difference between AMT and regular tax income or loss) . . . . . . . . . . 19
# 20 Loss limitations (difference between AMT and regular tax income or loss) . . . . . . . . . . . 20
# 21 Circulation costs (difference between regular tax and AMT) . . . . . . . . . . . . . . . 21
# 22 Long-term contracts (difference between AMT and regular tax income) . . . . . . . . . . . 22
# 23 Mining costs (difference between regular tax and AMT) . . . . . . . . . . . . . . . . 23
# 24 Research and experimental costs (difference between regular tax and AMT) . . . . . . . . . . 24
# 25 Income from certain installment sales before January 1, 1987 . . . . . . . . . . . . . . 25 ( )
# 26 Intangible drilling costs preference . . . . . . . . . . . . . . . . . . . . . . . 26
# 27 Other adjustments, including income-based related adjustments . . . . . . . . . . . . . 27

amt_income=cell(28, "Alternative minimum taxable income. (PI)",
"CV('agi_minus_ded') + CV('amt_medical') + CV('taxes_deducted') + CV('mort_interest_adjustment') + CV('misc_deductions') + CV('amt_deduction_deduction') + CV('amt_refund_deduction') + CV('amt_investment_expense_deduction') + CV('amt_depletion_deduction') + CV('nold') + CV('amt_nold')",
('agi_minus_ded', 'amt_medical', 'taxes_deducted', 'mort_interest_adjustment', 'misc_deductions', 
'amt_deduction_deduction', 'amt_refund_deduction', 'amt_investment_expense_deduction', 'amt_depletion_deduction', 
'nold', 'amt_nold')), 
amt_exemption=cell(29, "AMT exemption", "get_amt_exemption(CV('amt_income'))", ('amt_income',)),
amt_in_minus_exemption=cell(30, "AMT income minus exemption",
    "CV('amt_income')-CV('amt_exemption')", ('amt_income', 'amt_exemption')),

#30 Subtract line 29 from line 28. If more than zero, go to line 31. If zero or less, enter -0- here and on lines 31, 33, and 35, and go to line 34 . . . . . . . . . . . . . . . . . . . . . . . . . . 30

amt_preftc=cell(31, "Tentative AMT pre-FTC (PI)", "get_tamt(CV('amt_in_minus_exemption'))",('amt_in_minus_exemption',)),
amt_ftc=cell(32, "AMT foreign tax credit (UI)", '0'),
amt_tentative=cell(33, "Tentative AMT", "CV('amt_preftc')-CV('amt_ftc')", ('amt_preftc', 'amt_ftc')),
tax_from_1040=cell(34, "Tax from F1040", "CV('tax')+CV('credit_repayment')-CV('ftc')", ('tax', 'credit_repayment','ftc')),
amt=cell(35, "AMT", "max(CV('amt_tentative') - CV('tax_from_1040'), 0)", ('amt_tentative','tax_from_1040'))
)
