#2014 tax rate schedules
def tax_calc(inval):
    if inval < 9075: return .1*907.50
    if inval < 36900: return 907.50  + .15*(inval-9075)
    if inval < 89350: return 5081.25 + .25*(inval-36900)
    if inval < 186350: return 18193.75 + .28*(inval-89350)
    if inval < 405100: return 45353.75 + .33*(inval-186350)

f1040 = dict(
taxable_income = cell('taxable income', 55, '1', (None)),
tax = cell('tax', 56, "tax_calc(CV('taxable_income'))", ('taxable_income',)),
withheld = cell('withheld', 57, 'withheld_fed', (None), 'u'),
owed = cell('taxes owed', 58, 'CV("tax")-CV("withheld") if (CV("withheld") < CV("tax")) else 0', ('withheld', 'tax'))
)

