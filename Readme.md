py1040
======

This is a tax calculator for one individual U.S. tax return---Internal Revenue Service form 1040 (2015).

![basic output from the program](https://pbs.twimg.com/media/Cd7J1GlUIAAYb1I.jpg)
Image via: https://twitter.com/konklone/status/711227705996550145

### Quick start

0. Build it, via `make`. This will pull a copy of 1040.js [ See
   https://b-k.github.io/1040.js for the attractive front end], and generate
   Python versions of the forms.
1. Run `python3 taxes.py`, which will generate a file named `interview.py`.
2. Open `interview.py` in your text editor, and follow the instructions to provide
   information about your tax situation.
3. Run `python3 taxes.py` again. It will generate `inform.py`.
4. Open `inform.py` and fill in the information from your W-2s and other such sources.
5. Run `python3 taxes.py` again. It will calculate your taxes and print the line-by-line
   calculations to the screen.


### How and why

There are two ways to view a tax return. The first is as a form, as printed by the
IRS for a century. Because a key goal is to allow users to fill in their tax forms,
this is what the final output has to look like.

The second view is as a dependency tree. We want to calculate a single value: taxes
owed or refunded, but to find that value, we need to find taxes, which means we need
to calculate AGI and credits, and so on back to the original user data. This is the
internal format by which this script represents taxes.

In short, having the directed acyclic graph (DAG) underlying the tax forms lets us do real
work that would be onerous or painful using the form view.  By re-presenting the tax
calculation as a tree, we have the ability to trace back what led to any surprises
on the tax form, aggregate multiple users, and otherwise process the information
in a manner that would be difficult or incoherent using only the form view. If your
financial situation gives you the freedom to act on what-if scenarios, or if you are
a tax researcher considering the situations of diverse taxpayers, the structures here
are hopefully more amenable to your needs.

### Contributing

Each form is represented as a file holding a dictionary of cells, where each cell
represents a line of the tax code. The cell includes the text to print, the line number,
the calculation to do, whether the cell needs to be part of `inform.py`, and the list of
the cell's parent cells.

Adding a form, then, consists of transcribing this information for each needed line. This
is straightforward, and has proven to take only a few seconds per line.
We considered using the XML schemata here:
https://www.irs.gov/Tax-Professionals/e-File-Providers-&-Partners/Schemas-Business-Rules-and-Release-Memo-for-MeF-Form-1040-Series-Tax-Year-2015-Version-3_1
but it turns out to be easier to just cut/paste/modify the lines from the PDF forms.
Each form should be in one file in the `forms` directory, which has one python `dict` that
has the same name as the file (and optionally other initializations).

On the features-wanted list: a web-friendly front-end and better visualizations (say, the graph
with cells sized by their dollar value, so a viewer could immediately trace where the
bulk of income or expenses comes from).


### Caveats

This program is not a tax tutor or advisor; there are many other sources that can
help you optimize your tax situation. This is just a calculator.

There are many elements of the system that are not yet implemented. I (BK) am not
self-employed and don't have a farm, so I have not implemented Schedules C or F.
As above, contributing a new form or worksheet is not a massive effort, and if a few more
people contribute their situations, we may begin to have a reasonably complete and
accurate tax calculator. Until then, please bear in mind that you should verify every
calculation done here.

Please note this section from the license, which the license authors felt was important
enough to put in all-caps:

> THERE IS NO WARRANTY FOR THE PROGRAM, TO THE EXTENT PERMITTED BY APPLICABLE LAW.
> EXCEPT WHEN OTHERWISE STATED IN WRITING THE COPYRIGHT HOLDERS AND/OR OTHER PARTIES
> PROVIDE THE PROGRAM "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR IMPLIED,
> INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
> FOR A PARTICULAR PURPOSE.  THE ENTIRE RISK AS TO THE QUALITY AND PERFORMANCE OF THE
> PROGRAM IS WITH YOU.

This version was written by BK over the course of a weekend at home, and is therefore not
endoresed by or otherwise related to his employer.
