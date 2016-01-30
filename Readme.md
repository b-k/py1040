tax.readme

This is a tax calculator for one individual U.S. tax return---Internal Revenue Service form 1040.

quick start

Using this script to do your taxes is a two-step process. First, open `interview.py`,
which has a series of variables describing different tax-relevant situations (for
example, how many dependents do you have? Do you own a house?).  After you fill in
`interview.py`, run `generate_inform.py`.

You now have `inform.py`, which has all of the fields needed to complete
your taxes, given your tax situation as per `interview.py`. Gather your
papers and fill in all of the numbers here.

Then run `do_taxes.py` to print all of the information for your tax forms.

To summarize:

1. Fill in `interview.py`
2. Run `generate_inform.py`
3 Fill in `inform.py`
4. Run `do_taxes.py`


This runs through the decision tree to find all user inputs that are
needed for the given situation. Then the user fills in all of these
fields, and runs do_taxes.py. Because all dependencies are satisfied,
the tax forms can be completed and displayed to the screen.

Can I trust it?  This program is not a tax attorney, and was written by
humans. You are encouraged to understand your own tax situation yourself,
using this program as one view of the many available. It was written by
mortals, and could have bugs. Please note this section from the license,
which the license authors felt was important enough to put in all-caps:



How

There are two ways to view a tax return The first is as a form, as printed
by the IRS for a century. Because a key goal is to allow users to fill
in their tax forms, this is what the final output has to look like.

The second view is as a dependency tree. We want to calculate a single
value: taxes owed or refunded, but to find that value, we need to find
taxes, which means we need to calculate AGI and credits, and so on back
to the original user data. This is the internal format by which taxes
are represented.


Why?

I [BK] originally wrote this because my taxes are complicated and I needed
something to do the math. But by re-presenting the tax calculation as
a tree, we have the ability to trace back what led to any surprises
on the tax form, aggregate multiple users, and otherwise process the
information in a manner that would be difficult or incoherent using
only the form view. If your financial situation gives you the freedom
to act on what-if scenarios, or if you are a tax researcher considering
the situations of diverse taxpayers, the structures here are hopefully
more amenable to your needs.


Structures

The core structure is a cell: a single blank on a tax form. There are
three types: * calculated: a deterministic function of the previous nodes,
where future nodes depend on this node.  * display: This element has
no dependencies, but is an informational line that users have to fill
in anyway.  * user: a number provided by the user
