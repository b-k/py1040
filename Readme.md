py1040
======

This is a tax calculator for one individual U.S. tax return---Internal Revenue Service form 1040.

Quick start
-----------

1. Run `python taxes.py`. It will generate a file named `interview.py`.
2. Open `interview.py` in your text editor, and follow the instructions to provide
   information about your tax situation.
3. Run `python taxes.py` again. It will generate `inform.py`.
4. Open `inform.py` and fill in the information from your W-2s and other such sources.
5. Run `python taxes.py` again. It will calculate your taxes and print the line-by-line
   calculations to the screen.


How and why
-----------

There are two ways to view a tax return The first is as a form, as printed by the
IRS for a century. Because a key goal is to allow users to fill in their tax forms,
this is what the final output has to look like.

The second view is as a dependency tree. We want to calculate a single value: taxes
owed or refunded, but to find that value, we need to find taxes, which means we need
to calculate AGI and credits, and so on back to the original user data. This is the
internal format by which taxes are represented.

In short, having the directed acyclic graph underlying the tax forms lets us do real
work that would be onerous or painful using the form view.  By re-presenting the tax
calculation as a tree, we have the ability to trace back what led to any surprises
on the tax form, aggregate multiple users, and otherwise process the information
in a manner that would be difficult or incoherent using only the form view. If your
financial situation gives you the freedom to act on what-if scenarios, or if you are
a tax researcher considering the situations of diverse taxpayers, the structures here
are hopefully more amenable to your needs.

Can I trust it?
---------------

At the moment, it's a version-zero draft for discussion; see below about helping to
get it more functional. It seems like we could get it to work well for most tax situations
without too much further effort.

This program is not a tax tutor or advisor; there are many, many other sources that can
help you optimize your tax situation. This is just a calculator. Because it's very
incomplete right now, many tax situations are handled with zeros.

Please note this section from the license, which the license authors felt was important
enough to put in all-caps:

> THERE IS NO WARRANTY FOR THE PROGRAM, TO THE EXTENT PERMITTED BY APPLICABLE LAW.
> EXCEPT WHEN OTHERWISE STATED IN WRITING THE COPYRIGHT HOLDERS AND/OR OTHER PARTIES
> PROVIDE THE PROGRAM "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR IMPLIED,
> INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
> FOR A PARTICULAR PURPOSE.  THE ENTIRE RISK AS TO THE QUALITY AND PERFORMANCE OF THE
> PROGRAM IS WITH YOU.  SHOULD THE PROGRAM PROVE DEFECTIVE, YOU ASSUME THE COST OF ALL
> NECESSARY SERVICING, REPAIR OR CORRECTION.

Contributing
------------

Each form is represented as a file holding a dictionary of cells, where each cell
represents a line of the tax code. The cell includes the text to print, the line number,
the calculation to do, whether the cell needs to be part of `inform.py`, and the list of
the cell's parent cells.

Adding a form, then, consists of transcribing this information for each needed line. This
is straightforward, and has proven to take only a few seconds per line.
You will need to modify the list of parent cells in at least one already-existing cell.

Then, add a line to `taxes.py` to read in your form (you'll find the other form read-ins
to copy/paste/modify).

Conditionally-handled cells (like not printing mortgage expenses for people who don't own a
house) aren't yet implemented.
