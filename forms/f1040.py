#2014 tax rate schedules
def tax_calc(inval):
    if inval < 9075: return .1*907.50
    if inval < 36900: return 907.50  + .15*(inval-9075)
    if inval < 89350: return 5081.25 + .25*(inval-36900)
    if inval < 186350: return 18193.75 + .28*(inval-89350)
    if inval < 405100: return 45353.75 + .33*(inval-186350)

f1040 = dict(
exemptions=cell('exemptions', 6, 'exemptions', flag='u'),
wages=cell("Wages, salaries, tips, from form W-2", 7, 'wages', flag='u'),
interest=cell("Taxable interest", 8, 'interest', flag='u'),
tax_free_interest=cell("Tax-exempt interest", 8.5, 'tax_free_interest', flag='u'),
dividends=cell("Ordinary dividends", 9 , 'dividends', flag='u'),
qualified_dividends=cell("Qualified dividends", 9.5, 'qualified_dividends', flag='u'),
taxable_tax_refunds=cell("Taxable refunds, credits, or offsets of state and local income taxes", 10, 'taxable_tax_refunds', flag='u'),
alimony=cell('Alimony received', 11, 'alimony', flag='u'),
sched_c=cell('Schedule C business income', 12, '0'),
cap_gains=cell("Capital gains", 13, 'cap_gains', flag='u'),
noncap_gains=cell("Other gains or (losses), from Form 4797", 14, '0'),
ira=cell("IRA distributions", 15, 'ira_income', flag='u'),
taxable_ira=cell("Taxable IRA distributions", 15.5, 'taxable_ira_income', flag='u'),
pension=cell("Pensions and annuities",16, 'pension', flag='u'),
taxable_pension=cell("Pensions and annuities",16.5, 'taxable_pension', flag='u'),
rents_and_royalties=cell("Rents and royalties (&c) from Schedule E", 17, '0'),
farm_income=cell("Farm income from Schedule F", 18, '0'),
unemployment=cell("Unemployment compensation", 19, 'unemployment', flag='u'),
ss_benefits=cell("Social security benefits", 20, 'ss_benefits', flag='u'),
taxable_ss_benefits=cell("Taxable social security benefits", 20.5, 'taxable_ss_benefits', flag='u'),
other_in=cell("Other income.", 21, 'other_in', flag='u'),

total_in=cell("Total income", 22, 
"CV('wages') + CV('interest') + CV('dividends') + CV('taxable_tax_refunds') + CV('alimony') + CV('sched_c') + CV('cap_gains') +CV('taxable_ira') + CV('taxable_pension') + CV('rents_and_royalties') + CV('farm_income') + CV('unemployment') + CV('taxable_ss_benefits') + CV('other_in')",
('wages', 'interest', 'dividends', 'taxable_tax_refunds', 'alimony', 'sched_c', 'cap_gains','taxable_ira', 'taxable_pension','rents_and_royalties', 'farm_income', 'unemployment', 'taxable_ss_benefits', 'other_in')),

#Adjusted Gross Income
#23 Educator expenses . . . . . . . . . . . 23
#24 Certain business expenses of reservists, performing artists, and
#fee-basis government officials. Attach Form 2106 or 2106-EZ 24
#25 Health savings account deduction. Attach Form 8889 . 25
#26 Moving expenses. Attach Form 3903 . . . . . . 26
#27 Deductible part of self-employment tax. Attach Schedule SE . 27
#28 Self-employed SEP, SIMPLE, and qualified plans . . 28
#29 Self-employed health insurance deduction . . . . 29
#30 Penalty on early withdrawal of savings . . . . . . 30
#31a Alimony paid b Recipient’s SSN ▶ 31a
#32 IRA deduction . . . . . . . . . . . . . 32
#33 Student loan interest deduction . . . . . . . . 33
#34 Tuition and fees. Attach Form 8917 . . . . . . . 34
#35 Domestic production activities deduction. Attach Form 8903 35
#36 Add lines 23 through 35 . . . . . . . . . . . . . . . . . . . 36

subtractions_from_income=cell("Sum of subtractions from gross income", 36, '0'),
AGI=cell("Adjusted gross income", 37, "CV('total_in') - CV('subtractions_from_income')",
('total_in', 'subtractions_from_income')),
agi_again=cell("Adjusted gross income, again", 38, "CV('AGI')", ('AGI')),


taxable_income = cell('taxable income', 55, 'AGI', ('AGI')),
tax = cell('tax', 56, "tax_calc(CV('taxable_income'))", ('taxable_income',)),
withheld = cell('withheld', 57, 'withheld_fed', (None), 'u'),
owed = cell('taxes owed', 58, 'CV("tax")-CV("withheld") if (CV("withheld") < CV("tax")) else 0', ('withheld', 'tax'))
)
