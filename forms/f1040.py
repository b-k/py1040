
exemption_multiplier=4000  #changes annually

#2014 tax rate schedules
def tax_calc(inval):
    if inval < 9075: return .1*907.50
    if inval < 36900: return 907.50  + .15*(inval-9075)
    if inval < 89350: return 5081.25 + .25*(inval-36900)
    if inval < 186350: return 18193.75 + .28*(inval-89350)
    if inval < 405100: return 45353.75 + .33*(inval-186350)

def eitc(income, kids):
    #See http://www.taxpolicycenter.org/taxfacts/displayafact.cfm?Docid=36 
    #phase-in rate, plateu start, plateu value, plateu end, phase-out rate, zero point
    data=[[7.65, 6610, 506, 8270, 7.65, 14880],
          [34, 9920, 3373,  18190, 15.98, 39296],
          [40, 13931, 5572, 18190, 21.06, 44648],
          [45, 13930, 6269, 18190, 21.06, 47955]]
    row=kids if kids <=3 else 3
    if income < 0: print("Negative income! (%s) Please fix." % (income,))
    if income >= data[row][5]: return 0
    if income >= data[row][3]: return income*data[row][4]/100.
    if income <= data[row][1]: return income*data[row][0]/100.
    return data[row][2]


def deductions():
    ded=0
    if status=="married" or status=="single":
        ded=6300
    elif status=="married filing jointly":
        ded=12600
    elif status=="head of household":
        ded=9250
    if itemizing:
        ded=max(ded, CV('total_itemized_deductions'))
    return ded

f1040 = dict(
exemptions=cell('exemptions', 6, flag='u'),
income_divider=cell('>>>>>>>>>>>> Income                                   ', 6.9, '0'),
wages=cell("Wages, salaries, tips, from form W-2", 7, flag='u'),
interest=cell("Taxable interest", 8, flag='u'),
tax_free_interest=cell("Tax-exempt interest", 8.5, flag='uo'),
dividends=cell("Ordinary dividends", 9, flag='u'),
qualified_dividends=cell("Qualified dividends", 9.5, flag='u'),
taxable_tax_refunds=cell("Taxable state/local income tax refunds/credits/offsets", 10, flag='u'),
alimony=cell('Alimony received', 11, flag='uo'),
sched_c=cell('Schedule C business income', 12, '0'),
cap_gains=cell("Capital gains", 13, flag='u'),
noncap_gains=cell("Other gains or (losses), from Form 4797 (not implemented)", 14, '0', flag='o'),
ira_income=cell("IRA distributions", 15, flag='uo'),
taxable_ira_income=cell("Taxable IRA distributions", 15.5, flag='uo'),
pension=cell("Pensions and annuities",16, flag='uo', situation='over_65 or spouse_over_65'),
taxable_pension=cell("Pensions and annuities",16.5, flag='uo', situation='over_65 or spouse_over_65'),
rents_and_royalties=cell("Rents and royalties (&c) from Schedule E", 17, 'CV("rr_income") if have_rr else 0', ('rr_income',), flag='o'),
farm_income=cell("Farm income from Schedule F (not implemented)", 18, '0', flag='o'),
unemployment=cell("Unemployment compensation", 19, flag='uo'),
ss_benefits=cell("Social security benefits", 20, flag='uo', situation='over_65 or spouse_over_65'),
taxable_ss_benefits=cell("Taxable social security benefits", 20.5,
                            flag='uo', situation='over_65 or spouse_over_65'),
other_in=cell("Other income.", 21, flag='uo'),

magi_total_in=cell("Total income for MAGI (PI)", 0, 
"CV('wages') + CV('interest') + CV('dividends') + CV('taxable_tax_refunds') + CV('alimony') + CV('sched_c') + CV('cap_gains') +CV('taxable_ira_income') + CV('taxable_pension') + CV('farm_income') + CV('unemployment') + CV('taxable_ss_benefits') + CV('other_in')",
('wages', 'interest', 'dividends', 'taxable_tax_refunds', 'alimony', 'sched_c', 'cap_gains','taxable_ira_income', 'taxable_pension','rents_and_royalties', 'farm_income', 'unemployment', 'taxable_ss_benefits', 'other_in')),

total_in=cell("Total income", 22, "CV('magi_total_in') + CV('rents_and_royalties')",
('magi_total_in','rents_and_royalties')),

agi_divider=cell('>>>>>>>>>>>> AGI                                   ', 22.9, '0'),

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

t_and_i_divider=cell('>>>>>>>>>>>> Taxes and income                      ', 36.9, '0'),
MAGI=cell("Modified adjusted gross income", 0, "CV('magi_total_in') - CV('subtractions_from_income')",
('magi_total_in', 'subtractions_from_income')), 
AGI=cell("Adjusted gross income", 37, "CV('total_in') - CV('subtractions_from_income')",
('total_in', 'subtractions_from_income')),
agi_again=cell("Adjusted gross income, again", 38, "CV('AGI')", ('AGI',)),

#39 elderly, blind

deductions=cell('Deductions', 40, 'deductions()', ('total_itemized_deductions',)),
agi_minus_deductions=cell("AGI minus deductions", 41,
			'CV("agi_again") - CV("deductions")', ('agi_again', 'deductions')),
exemption_amount=cell("Exemption amount", 42, 'exemptions*exemption_multiplier'),
taxable_income=cell("Taxable income", 43,
	'max(CV("agi_minus_deductions")-CV("exemption_amount"), 0)',
	('agi_minus_deductions', 'exemption_amount')),
tax=cell("Tax", 44, 'tax_calc(CV("taxable_income"))', ('taxable_income',)),
#45 Alternative minimum tax (see instructions). Attach Form 6251 . . . . . . . . . 45
#46 Excess advance premium tax credit repayment. Attach Form 8962 . . . . . . . . 46
pretotal_tax=cell("Tax + AMT + F8962", 47, 'CV("tax")', ('tax',)),
#48 Foreign tax credit. Attach Form 1116 if required . . . . 48
#49 Credit for child and dependent care expenses. Attach Form 2441 49
#50 Education credits from Form 8863, line 19 . . . . . 50
#51 Retirement savings contributions credit. Attach Form 8880 51
#52 Child tax credit. Attach Schedule 8812, if required . . . 52
#53 Residential energy credits. Attach Form 5695 . . . . 53
#54 Other credits from Form: a 3800 b 8801 c 54
total_credits=cell("Total credits", 55, '0'),
tax_minus_credits=cell("Tax minus credits", 56,
	'max(CV("pretotal_tax")-CV("total_credits"), 0)', ('pretotal_tax', 'total_credits')),

#57 Self-employment tax. Attach Schedule SE 
#58 Unreported social security and Medicare tax from Form: a 4137 b 8919
#59 Additional tax on IRAs, other qualified retirement plans, etc. Attach Form 5329 if required
#60 a Household employment taxes from Schedule H
#b First-time homebuyer credit repayment. Attach Form 5405 if required

obamacare_fee=cell("Health care individual responsibility", 61, '0'),

#62 Taxes from: a Form 8959 b Form 8960 c Instructions; enter code(s) 62
total_tax=cell("Total tax", 63, 'CV("tax_minus_credits") + CV("obamacare_fee")', 
		    ("tax_minus_credits", "obamacare_fee")),
federal_tax_withheld=cell("Federal income tax withheld from Forms W-2 and 1099", 64, flag='u'),

payments_divider=cell('>>>>>>>>>>>> Payments                              ', 63.9, '0'),
#65 2015 estimated tax payments and amount applied from 2014 return 65
eitc=cell("Earned income credit (EIC)", 66.5, 'eitc(CV("agi_again"), kids)', ('agi_again',)),
#b Nontaxable combat pay election 66b
#67 Additional child tax credit. Attach Schedule 8812 . . . . . 67
#68 American opportunity credit from Form 8863, line 8 . . . 68
#69 Net premium tax credit. Attach Form 8962 . . . . . . 69
#70 Amount paid with request for extension to file . . . . . 70
#71 Excess social security and tier 1 RRTA tax withheld . . . . 71
#72 Credit for federal tax on fuels. Attach Form 4136 . . . . 72
#73 Credits from Form: a 2439 b Reserved c 8885 d 73
total_payments=cell("Total payments", 74, 'CV("federal_tax_withheld")+CV("eitc")', ('federal_tax_withheld','eitc')),
refund=cell("Refund!", 75, 'max(CV("total_payments")-CV("total_tax"), 0)'
                         , ('total_tax', 'total_payments')),
tax_owed=cell("Tax owed", 78, 'max(CV("total_tax")-CV("total_payments"), 0)'
                            , ('total_tax', 'total_payments')),
)
