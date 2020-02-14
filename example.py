# This code does not run, it is just an example

from tablewriter import TableWriter

writer = TableWriter(
    data=df,
    caption="Caption to display in LateX",
    label="label one can use to reference this table in Latex",
    to_latex_args={"escape": True, "any_valid_to_latex_method_argument": value},
    paperwidth=25,  # width of the pdf. Optionnal, but automatic width sometime fails
    paperheight=15,  # same remark as above
    hide_numbering=True,  # Do not show 'Table 1:' in caption
    number=2,  # Table number for 'Table n:' in caption. Useless if hide_numbering=True,
               # but shown for example
    path="output_file",  # path to the output file. Extension does not matter.
    read_args={"path": "path_to_a_csv_or_excel", "index_col": 0},  # read a dataframe from a csv or excel
                                                                   # file using the specified arguments. 
                                                                   # Those must be valid for the read_csv 
                                                                   # or read_excel pandas method.
                                                                   # Overrides 'data' argument
    packages={"graphicx": {"dvipdfmx": None}, "lipsum":{}})  # LateX packages to use, with possible
                                                             # optionnal arguments and values for those
                                                             # arguments

# Compile the .tex and produce and .pdf. Silenced removes LateX terminal output, recreate will recreate
# the .tex file (otherwise is read instead), clean will remove all the .aux, .log, etc... files,
# clean_tex also removes the .tex file, leaving only the .pdf and possible .csv/.excel files
# WARNING : if clean=True, removes all files with same name as path.name that do not end in .pdf, .tex,
# .csv or .excel
# The values for the arguments below are the default values
writer.compile(silenced=True, recreate=True, clean=True, clean_tex=False)
