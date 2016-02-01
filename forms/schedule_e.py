#sum losses from royalties to possibly limited real estate losses
def rrlosses(rents, royalties, net, real_loss):
    if isinstance(net, tuple):
        total = 0
        for i in range(0, len(net)):
            if net[i]<0 and royalties[i]>0: total = total + net[i]
            if real_loss[i]<0: total = total + real_loss[i]
    else:
        if rents > 0: return real_loss
        else:         return net

schedule_e=dict(
rents_received=cell("Rents received [may be an array]", 3, flag='u'),
royalties_received=cell("Royalties received", 4, flag='u'),
sched_e_expenses_header =cell(">>>>>>>>>>> expenses            ", 4.9),

advertising = cell("Advertising", 5, flag='u'),
auto_and_travel = cell("Auto and travel", 6, flag='u'),
sched_e_cleaning_and_maintenance = cell("Cleaning and maintenance", 7, flag='u'),
sched_e_commissions = cell("Commissions", 8, flag='u'),
sched_e_insurance = cell("Insurance", 9, flag='u'),
sched_e_professional_fees = cell("Legal and other professional fees", 10, flag='u'),
sched_e_management_fees = cell("Management fees", 11, flag='u'),
sched_e_mortgage_interest = cell("Mortgage interest paid to banks, etc", 12, flag='u'),
sched_e_other_interest = cell("Other interest", 13, flag='u'),
sched_e_repairs = cell("Repairs", 14, flag='u'),
sched_e_supplies = cell("Supplies", 15, flag='u'),
sched_e_taxes = cell("Taxes", 16, flag='u'),
sched_e_utilities = cell("Utilities", 17, flag='u'),
sched_e_depreciation = cell("Depreciation expense or depletion", 18, flag='u'),
sched_e_other_expenses = cell("Other", 19, flag='u'),
sched_e_total_expenses = cell("Total expenses", 20,
"CV('advertising') + CV('auto_and_travel') + CV('sched_e_cleaning_and_maintenance') + CV('sched_e_commissions') +  \
CV('sched_e_insurance') + CV('sched_e_professional_fees') + CV('sched_e_management_fees') + CV('sched_e_mortgage_interest') +  \
CV('sched_e_other_interest') + CV('sched_e_repairs') + CV('sched_e_supplies') + CV('sched_e_taxes') +  \
CV('sched_e_utilities') + CV('sched_e_depreciation') + CV('sched_e_other_expenses')",
('advertising', 'auto_and_travel', 'sched_e_cleaning_and_maintenance', 'sched_e_commissions', 'sched_e_insurance', 
'sched_e_professional_fees', 'sched_e_management_fees', 'sched_e_mortgage_interest', 'sched_e_other_interest', 
'sched_e_repairs', 'sched_e_supplies', 'sched_e_taxes', 'sched_e_utilities', 'sched_e_depreciation', 'sched_e_other_expenses')),

net_rr=cell("Rents/royalties minus expenses", 21, "CV('rents_received') + CV('royalties_received')-CV('sched_e_total_expenses')",
('rents_received', 'royalties_received', 'sched_e_total_expenses')),

deductible_rr_losses=cell("Deductible rental real estate loss after (unimplemented) limitation", 22, 'min(CV("net_rr"), 0)',('net_rr',)),

sched_e_sum3=cell("Total for line 3 for all rentals", 23.0, "sum(CV('rents_received'))", ('rents_received',)),
sched_e_sum4=cell("Total for line 4 for all royaltys", 23.2, "sum(CV('royalties_received'))", ('royalties_received',)),
sched_e_sum12=cell("Total for line 12 for all propertiess", 23.4, "sum(CV('sched_e_mortgage_interest'))", ('sched_e_mortgage_interest',)),
sched_e_sum18=cell("Total for line 18 for all propertiess", 23.6, "sum(CV('sched_e_depreciation'))", ('sched_e_depreciation',)),
sched_e_sum20=cell("Total for line 20 for all propertiess", 23.8, "sum(CV('sched_e_total_expenses'))", ('sched_e_total_expenses',)),

sched_e_income=cell("Positive Income.", 24, "CV('net_rr') if not isinstance(CV('net_rr'), tuple) else sum([x for x in CV('net_rr') if x>0])", ('net_rr',)),
sched_e_losses=cell("Royalty losses plus possibly limited rental losses", 25,
    'rrlosses(CV("rents_received"), CV("royalties_received"), CV("net_rr"), CV("deductible_rr_losses"))',
    ("rents_received", "royalties_received", "net_rr", "deductible_rr_losses")),
rr_income=cell("Total rents and royalties", 26, 'CV("sched_e_income")+CV("sched_e_losses")', ('sched_e_income', 'sched_e_losses')) 
)

for i in schedule_e.values():
    i.situation = i.situation and have_rr
