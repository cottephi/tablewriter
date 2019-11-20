import pandas as pd
from pathlib import Path
import tablewriter as tw
tw.TableWriter.set_verbose(1)

writer = tw.TableWriter(path="./test.tex",
                        col_names = ["chie_n", "cha^t"],
                        row_names = ["puces", "tiques", "verres"],
                        data = [["41", "\\textcolor{red}{53}"],
                                ["62", "\\textcolor{red}{103}"],
                                ["3", "\\textcolor{red}{7}"]],
                        escape_special_chars = True)
writer.set_line(["4","7"], name = "poils")
writer.set_column(["1","2","3","4"], name="rat")
writer.compile_pdf_file()

writer2 = tw.TableWriter(path="./test2.tex",
                        caption = "un test!",
                        label = "tab::un-test",
                        data = pd.DataFrame(
                            columns = ["chien", "chat"],
                            index = ["puces", "tiques", "verres"],
                            data=[["41", "\\textcolor{red}{53}"],
                                    ["62", "\\textcolor{red}{103}"],
                                    ["3", "\\textcolor{red}{7}"]]))
writer2.set_line(["4","7"], name = "poils")
writer2.set_column(["1","2","3","4"], name="rat")
writer2.compile_pdf_file(silenced = True)
