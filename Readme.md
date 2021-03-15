py1040
======

This is a tax calculator for one individual U.S. tax return—Internal Revenue Service form 1040 (2015).


First, you will take a short interview:
![An interview form, actually a standard Python file with assignments like `status="married"` and `over_65=False`](interview.png)

This will generate a personalized list of inputs for you to provide:
![Another standard Python file with lines for variables with names like `1040_wages` and `f1040_interest`. Lines are documented with comments.](input_form.png)

From those, you will get output that roughly follows the tax forms:
![Output, headed "Form 1040". Each line has a line number from the IRS form, a title like `taxable interest` and `tax minus credits`.](final_form.png)

### Quick start

0. Build it, via `make`. This will pull a copy of 1040.js (See
   https://b-k.github.io/1040.js for the attractive front end), and generate
   Python versions of the forms.
1. Run `python3 taxes.py`, which will generate a file named `interview.py`.
2. Open `interview.py` in your text editor, and follow the instructions to provide
   information about your tax situation.
3. Run `python3 taxes.py` again. It will generate `inform.py`.
4. Open `inform.py` and fill in the information from your W-2s and other such sources.
5. Run `python3 taxes.py` again. It will calculate your taxes and print the line-by-line
   calculations to the screen.
   

### Caveats

This program is not a tax tutor or advisor; there are many other sources that can
help you optimize your tax situation. This is just a calculator, that may be useful in
the process.

There are many elements of the system that are not yet implemented. The lead author is not
self-employed and doesn't have a farm, so Schedules C and F are not implemented.
As discussed below, contributing a new form or worksheet is not a massive effort, and if a few more people contribute their situations, we may begin to have a reasonably complete and accurate tax calculator. Until then, please bear in mind that you should verify every calculation done here.

Please note this section from the license, which the license authors felt was important
enough to put in all-caps:

> THERE IS NO WARRANTY FOR THE PROGRAM, TO THE EXTENT PERMITTED BY APPLICABLE LAW.  EXCEPT WHEN OTHERWISE STATED IN WRITING THE COPYRIGHT HOLDERS AND/OR OTHER PARTIES PROVIDE THE PROGRAM "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE.  THE ENTIRE RISK AS TO THE QUALITY AND PERFORMANCE OF THE PROGRAM IS WITH YOU.

This version was first written by BK over the course of a weekend at home, and is therefore not
endorsed by or otherwise related to his employer.


### Contributing

Each form is represented as a file holding a dictionary of cells, where each cell
represents a line of the tax code. The cell includes the text to print, the line number,
the calculation to do, whether the cell needs to be part of `inform.py`, and the list of
the cell's parent cells. That dictionary is at https://github.com/b-k/1040.js , in a
relatively language-independent format that both the Javascript and Python version parse
into functions.

Adding a form, then, consists of transcribing this information for each needed line. This
is straightforward, and has proven to take only a few seconds per line.
We considered using the XML schemata here:
https://www.irs.gov/Tax-Professionals/e-File-Providers-&-Partners/Schemas-Business-Rules-and-Release-Memo-for-MeF-Form-1040-Series-Tax-Year-2015-Version-3_1
but it turns out to be easier to just cut/paste/modify the lines from the PDF forms.
Each form should be in one file in the `forms` directory, which has one python `dict` that has the same name as the file (and optionally other initializations).
