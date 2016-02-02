def what_is_allowed(L5, L9):
    out=min(L5, L9)
    if (out < L5):
        print("%s in real estate losses are disallowed. Carry them over to next year." % (L5-out,))
    return out

f8582=dict(
ws1_8582_net_gain=cell(0.1,"Net income", 'CV("rents_received") if CV("rents_received") > 0 else 0', ('rents_received')),
ws1_8582_net_loss=cell(0.2,"Net loss", 'CV("rents_received") if CV("rents_received") < 0 else 0', ('rents_received')),
ws1_8582_prior_loss=cell(0.3,"Prior year carryover real estate loss", flag='u'),

div_85821=cell(0.9,">>>>Part I        "),
div_85822=cell(4.9,">>>>Part II       "),
f8582_net_in=cell(1.0, "Net income", "sum(CV('ws1_8582_net_gain')", ('ws1_8582_net_gain')),
f8582_net_loss=cell(1.2, "Net loss", "sum(CV('ws1_8582_net_loss')", ('ws1_8582_net_loss')),
f8582_carryover=cell(1.4, "Prior year carryover", "sum(CV('ws1_8582_prior_loss')", ('ws1_8582_prior_loss')),
f8582_total_real_in=cell(1.6, "Sum", "sum(CV('f8582_net_in') + CV('f8582_net_loss') + CV('f8582_carryover')", 
                        "('f8582_net_in', 'f8582_net_loss', 'f8582_carryover')"), 

f8582_commercial_revitalization=cell(2, "Commercial revitalization deductions (UI)", '0'),
f8582_passive_activities=cell(3, "Passive activity income (UI)", '0'),
f8582_total_in=cell(4, "Total in",  "sum(CV('f8582_total_real_in') + CV('f8582_commercial_revitalization') + CV('f8582_passive_activities')", ('f8582_total_real_in', 'f8582_commercial_revitalization', 'f8582_passive_activities')),

f8582_min = cell(5, "the smaller of the loss on line 1d or the loss on line 4",
    "min(CV('f8582_total_real_in'), CV('f8582_total_in'))", ('f8582_total_real_in', 'f8582_total_in')),
f8582_150k = cell(6, "150k", '150000'),
f8582_magi_again=cell(7, "MAGI if positive", "max(CV('MAGI'), 0)", ('MAGI')),

f8582_diff=cell(8, "Line 6 - Line 7", 'max(CV("f8582_magi_again")- CV("f8582_150k"), 0)', ("f8582_magi_again", "f8582_150k")),
f8582_half=cell(9, "Half of line 8, up to 25k", 'min(25000, CV("f8582_diff")/2.)', ('f8582_diff')),
allowed_real_losses=cell(10, "Allowed real estate losses",
    "what_is_allowed(CV('f8582_min'), CV('f8582_half'))", ('f8582_min', 'f8582_half')),

div_8582=cell(">>>>Total ", 14.9),
total_gains_8582=cell(15, "Total (UI)", '0'),
total_losses_8582=cell(16, "Total loss", "CV('allowed_real_losses')+CV('total_gains_8582')", ('allowed_real_losses', 'total_gains_8582'))
)
